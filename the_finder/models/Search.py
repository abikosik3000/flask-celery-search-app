from redis_om import JsonModel, Field
from typing import Optional, List
from pydantic import ValidationError
from the_finder.models.FilterSize import FilterSize
from the_finder.models.FilterCreationTime import FilterCreationTime
from the_finder import app
import os
import glob
import mmap
import zipfile
import fnmatch


class Search(JsonModel):
    text: Optional[str]
    file_mask: str = Field(default="*")
    size: Optional[FilterSize]
    creation_time: Optional[FilterCreationTime]
    finished: bool = Field(default=False)
    paths: List[str] = Field(default=list())

    @property
    def search_res(self):
        res = {"finished": self.finished}
        if self.finished:
            res.update({"paths": self.paths})
        return res

    def _chek_arhive(self, abspath_arhive):
        arhive = zipfile.ZipFile(abspath_arhive, "r")
        for file_info in arhive.infolist():

            if self._chek_arhive_file(file_info):
                self.paths.append(os.path.join(abspath_arhive, file_info.filename))
                self.save()

    def _chek_arhive_file(self, file: zipfile.ZipInfo):
        return True

    def _chek_file(self, abspath):

        if not self.size is None:
            if not self.size.chek_compilance(abspath):
                return False

        if not self.creation_time is None:
            if not self.creation_time.chek_compilance(abspath):
                return False

        with open(abspath, "rb", 0) as file, mmap.mmap(
            file.fileno(), 0, access=mmap.ACCESS_READ
        ) as s:
            if s.find(self.text.encode("utf-8")) == -1:
                return False

        return True

    def start_search(self):
        # for file_path in glob.iglob( '**/'+self.file_mask, root_dir=repo,recursive=True,):
        for root, dirs, files in os.walk(app.config["SEARCH_DIRECTORY"]):
            for file_name in files:
                abspath = os.path.join(root, file_name)

                if zipfile.is_zipfile(abspath):
                    self._chek_arhive(abspath)

                if self._chek_file(abspath):
                    self.paths.append(abspath)
                    self.save()

        self.finished = True
        self.save()

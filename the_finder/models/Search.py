import os
import mmap
import fnmatch
from zipfile import ZipFile, ZipInfo, is_zipfile

from redis_om import JsonModel, Field
from typing import Optional, List
from pydantic import StrictStr

from the_finder.models.FilterSize import FilterSize
from the_finder.models.FilterCreationTime import FilterCreationTime
from the_finder import app


class Search(JsonModel):
    '''the model that stores and performs the search'''
    text: Optional[StrictStr]
    file_mask: StrictStr
    size: Optional[FilterSize]
    creation_time: Optional[FilterCreationTime]
    finished: bool = Field(default=False)
    paths: List[str] = Field(default=list())

    @property
    def search_res(self) -> dict:
        '''Returns results of search'''
        res = {"finished": self.finished}
        if self.finished:
            res.update({"paths": self.paths})
        return res
    
    def search(self) -> None:
        '''searches for files by filtering conditions, 
        as well as searches for files in archives
        '''

        # we are looking through all the nested directories
        for root, dirs, files in os.walk(app.config["SEARCH_DIRECTORY"]):
            # we are looking through all files in directories
            for file_name in files:
                abspath = os.path.join(root, file_name)
                
                # if the file is an archive, it starts checking the archive
                if is_zipfile(abspath):
                    self._chek_arhive(abspath)
                
                # if the file has passed the filters, then add it to the search result
                if self._chek_file(abspath):
                    self.paths.append(abspath)
                    self.save()

        self.finished = True
        self.save()

    def _chek_file(self, abspath: str) -> bool:
        '''checking whether the file has passed the filters'''

        # checking glob mask
        if not fnmatch.fnmatch(os.path.basename(abspath), self.file_mask):
            return False

        # checking size file
        if not self.size is None:
            if not self.size.chek_compilance(abspath):
                return False

        # checking creation time file
        if not self.creation_time is None:
            if not self.creation_time.chek_compilance(abspath):
                return False

        # checking the occurrence of text in a file
        if not self.text is None:
            with open(abspath, "rb", 0) as file:
                #create a memory map for a faster search
                with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                    if s.find(self.text.encode("utf-8")) == -1:
                        return False
        return True
    
    def _chek_arhive(self, abspath_arhive) -> None:
        '''searches for files by filters in the archive'''

        arhive = ZipFile(abspath_arhive, "r", allowZip64=True)
        # checking all files in the archive
        for file_info in arhive.infolist():
            # skip folders
            if file_info.is_dir():
                continue
            
            # if the file has passed the filters, then add it to the search result
            if self._chek_arhive_file(file_info, arhive):
                self.paths.append(os.path.join(abspath_arhive, file_info.filename))
                self.save()

    def _chek_arhive_file(self, file: ZipInfo, arhive: ZipFile) -> bool:
        # checking glob mask
        if not fnmatch.fnmatch(os.path.basename(file.filename), self.file_mask):
            return False

        # checking size file
        if not self.size is None:
            if not self.size.chek_arhive_compilance(file):
                return False

        # checking creation time file
        if not self.creation_time is None:
            if not self.creation_time.chek_arhive_compilance(file):
                return False
        
        # checking the occurrence of text in a file
        if not self.text is None:
            with arhive.open(file.filename, "r") as fbin:
                # the file in the archive opens in bit representation
                if not self.text.encode("utf-8") in fbin.read():
                    return False
        return True
    

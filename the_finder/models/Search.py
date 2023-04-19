from redis_om import JsonModel , EmbeddedJsonModel, Field
from typing import Optional, List
from pydantic import PositiveInt, ValidationError
from abc import ABC, abstractmethod
from the_finder.models.FilterSize import FilterSize
from the_finder.models.FilterCreationTime import FilterCreationTime
from the_finder import app
import os
from os.path import join, getsize , getctime
import glob

class Search(JsonModel):
    text: Optional[str]
    file_mask: str = Field(default='*')
    size: Optional[FilterSize]
    creation_time: Optional[FilterCreationTime]
    finished: bool = Field(default= False)
    paths: List[str] = Field(default=list())

    @property
    def search_res(self):
        res = {'finished': self.finished}
        if(self.finished):
            res.update({'paths': self.paths})
        return res

    def _aply_filters(self,abpath):
        if(not self.size is None):
            if(not self.size.chek_compilance(abpath)):
                return False
        if(not self.creation_time is None):
            if(not self.creation_time.chek_compilance(abpath)):
                return False
        return True
      
    def start_search(self):
        repo = app.config['SEARCH_DIRECTORY']
        #chek .zip

        for file_path in glob.iglob( '**/'+self.file_mask, root_dir=repo,recursive=True):
            abspath = join(repo, file_path)
            if(not self._aply_filters(abspath)):
                continue
            #chek text
            print("winner")
            self.paths.append(abspath)
            self.save()
        
        self.finished = True
        self.save()

        
        
            
        
            



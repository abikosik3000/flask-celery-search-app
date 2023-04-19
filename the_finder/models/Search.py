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
      
    def start_search(self):
        #print(self)
        #print(app.config['SEARCH_DIRECTORY'])
        self._search_in_repo(app.config['SEARCH_DIRECTORY'])

    def _aply_filters(self,abpath):
        if(not self.size is None):
            if(not self.size.chek_compilance(abpath)):
                return False
            
        if(not self.creation_time is None):
            if(not self.creation_time.chek_compilance(abpath)):
                return False
        
        return True

    def _search_in_repo(self,repo):

        print(self.file_mask)
        for item in glob.iglob( self.file_mask, root_dir=repo,recursive=True):
            print(item)

        '''
        for root, dirs, files in os.walk(repo,followlinks=False):
            for file in files:
                abspath = join(root, file)
                size = getsize(abspath)
                timestamp = getctime(abspath)
                print(abspath, size, timestamp)
                if(self._aply_filters(abspath)):
                    pass
        '''
        
            
        
            



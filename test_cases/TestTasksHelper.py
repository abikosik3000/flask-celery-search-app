import sys
import time
import json
import unittest

sys.path.append("..")
from the_finder import app

class TestTaskHelper(unittest.TestCase):
    '''contains auxiliary methods for testing requests to the application '''
    
    RETRY_TIME = 0.25
    MAX_ATTEMPTS = 10

    def create_app_test_client(self):
        self.app = app.test_client()
        self.maxDiff = None
        self.app.get("/migrate")

    def send_post_with_json(self, url :str, data :dict):
        return self.app.post(url, data=json.dumps(data), content_type='application/json')
        
    def wait_result_task(self, search_key :str):
        '''they are waiting for the end of the search by pinging the server '''
        for _ in range(self.MAX_ATTEMPTS):
            response = self.app.get('/searches/' + search_key)
            if(response.get_json()['finished'] == True):
                return response
            time.sleep(self.RETRY_TIME)
            
        raise Exception('limit attempts exceeded')
    
        

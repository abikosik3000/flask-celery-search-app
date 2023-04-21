import unittest
import sys
import json

sys.path.append("..")
from the_finder import app
from the_finder.models.Search import Search


class TestUM(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.maxDiff = None
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def _postWithJSON(self, url :str, data :dict):
        return self.app.post(url, data=json.dumps(data), content_type='application/json')

    def test_404(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 404)

    def test_200(self):
        data = {"file_mask": "*"}
        response = self._postWithJSON("/search", data)
        self.assertEqual(response.status_code, 200)
    
    def test_no_data(self):
        data = {}
        response = self._postWithJSON("/search", data)
        self.assertEqual(response.status_code, 400)
    
    def test_400_incorrect_text(self):
        data = {
            "file_mask": "*",
            "text": 2,
        }
        response = self._postWithJSON("/search", data)
        body = response.get_json()

        self.assertEqual(body[0]['msg'], "str type expected")
        self.assertEqual(response.status_code, 400)

    def test_400_incorrect_text_multiply(self):
        data = {
            "file_mask": 1,
            "text": 1,
        }
        response = self._postWithJSON("/search", data)
        body = response.get_json()

        self.assertEqual(body[0]['msg'], "str type expected")
        self.assertEqual(body[1]['msg'], "str type expected")
        self.assertEqual(response.status_code, 400)

    def test_400_incorrect_creation_time(self):
        data = {
            "file_mask": "*",
            "creation_time": {"value": "2023-4404-21T00:00:00Z", "operator": "rt"},
        }
        response = self._postWithJSON("/search", data)
        body = response.get_json()

        self.assertEqual(body[0]['msg'], "operator must be in eq, gt, lt, ge, le")
        self.assertEqual(body[1]['msg'], "creation_time.value must be correct ISO 8601 datetime")
        self.assertEqual(response.status_code, 400)
    
    def test_400_incorrect_size(self):
        data = {
            "file_mask": "*",
            "size": { "operator": "rt"},
        }
        response = self._postWithJSON("/search", data)
        body = response.get_json()

        self.assertEqual(body[0]['msg'], "operator must be in eq, gt, lt, ge, le")
        self.assertEqual(body[1]['msg'], "field required")
        self.assertEqual(response.status_code, 400)

    def test_200_correct_id(self):
        data = {
            "file_mask": "*",
        }
        response = self._postWithJSON("/search", data)
        body = response.get_json()
        search_key = body['search_key']
        response2 = self.app.get('/searches/' + search_key)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_400_incorrect_id(self):
        response = self.app.get('/searches/a*()')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], "search id not found")

if __name__ == "__main__":
    unittest.main()

import unittest
import sys

sys.path.append("..")
from the_finder import app
from the_finder.models.Search import Search


class TestSearchModel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.maxDiff = None
        self.ctx.push()
        self.app.get("/migrate")

    def tearDown(self):
        self.ctx.pop()

    def test_mask_all(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/file3.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file3.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/note.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/screen.jpg",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/note.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/screen.jpg",
            ],
        }
        inp = {"file_mask": "*"}
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_mask_all_date_gt_210423(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
            ],
        }
        inp = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-21T00:00:00Z", "operator": "gt"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_mask_all_date_gt(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
            ],
        }
        inp = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-21T00:00:00Z", "operator": "gt"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_mask_all_date_eq(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/note.txt"
            ],
        }
        inp = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-19T15:28:30+03:00", "operator": "eq"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_mask_all_date_ge(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/note.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/note.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/screen.jpg",
            ],
        }
        inp = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_date_and_mask1(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file.bat",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
            ],
        }
        inp = {
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_date_and_mask2(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file1.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
            ],
        }
        inp = {
            "file_mask": "*file?.t??",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_date_mask_and_text(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
            ],
        }
        inp = {
            "text": "sad sad",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_date_mask_and_text(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
            ],
        }
        inp = {
            "text": "a",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_all_filters(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
            ],
        }
        inp = {
            "text": "a",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
            "size": {"value": 14, "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_null_res(self):
        true_res = {"finished": True, "paths": []}
        inp = {
            "text": "a",
            "file_mask": "*migfile*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
            "size": {"value": 14, "operator": "ge"},
        }
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)

    def test_jpeg_text(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/screen.jpg",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/screen.jpg",
            ],
        }
        inp = {"text": "cd", "file_mask": "*?", "size": {"value": 0, "operator": "ge"}}
        search = Search(**inp)
        search.search()
        self.assertEqual(search.search_res, true_res)


if __name__ == "__main__":
    unittest.main()

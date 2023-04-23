import unittest
import sys

from TestTasksHelper import TestTaskHelper

sys.path.append("..")
from the_finder import app
from the_finder.models.Search import Search


class TestSearchModel(TestTaskHelper):
    def setUp(self):
        self.create_app_test_client()

    def tearDown(self):
        pass

    def full_user_path(self, data , true_answ):
        response_create = self.send_post_with_json("/search", data)
        search_key = response_create.get_json()['search_key']
        response_result = self.wait_result_task(search_key)
        
        self.assertEqual(response_create.status_code, 200)
        self.assertEqual(response_result.status_code, 200)
        self.assertEqual(response_result.get_json(), true_answ)

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
        data = {"file_mask": "*"}
        self.full_user_path(data, true_res)

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
        data = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-21T00:00:00Z", "operator": "gt"},
        }
        self.full_user_path(data, true_res)

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
        data = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-21T00:00:00Z", "operator": "gt"},
        }
        self.full_user_path(data, true_res)

    def test_mask_all_date_eq(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/note.txt"
            ],
        }
        data = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-19T15:28:30+03:00", "operator": "eq"},
        }
        self.full_user_path(data, true_res)

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
        data = {
            "file_mask": "*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        self.full_user_path(data, true_res)

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
        data = {
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        self.full_user_path(data, true_res)

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
        data = {
            "file_mask": "*file?.t??",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        self.full_user_path(data, true_res)

    def test_date_mask_and_text(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file2.txt",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/file2.txt",
            ],
        }
        data = {
            "text": "sad sad",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        self.full_user_path(data, true_res)

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
        data = {
            "text": "a",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
        }
        self.full_user_path(data, true_res)

    def test_all_filters(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/file_now_create.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/file_now_create.zip",
            ],
        }
        data = {
            "text": "a",
            "file_mask": "*file*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
            "size": {"value": 14, "operator": "ge"},
        }
        self.full_user_path(data, true_res)

    def test_null_res(self):
        true_res = {"finished": True, "paths": []}
        data = {
            "text": "a",
            "file_mask": "*migfile*",
            "creation_time": {"value": "2023-04-19T15:16:10+03:00", "operator": "ge"},
            "size": {"value": 14, "operator": "ge"},
        }
        self.full_user_path(data, true_res)

    def test_jpeg_text(self):
        true_res = {
            "finished": True,
            "paths": [
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip/test_repo/folder/screen.jpg",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/test_repo.zip",
                "/home/abikosik3000/var/www/search_app/test_repo/folder/screen.jpg",
            ],
        }
        data = {"text": "cd", "file_mask": "*?", "size": {"value": 0, "operator": "ge"}}
        self.full_user_path(data, true_res)


if __name__ == "__main__":
    unittest.main()

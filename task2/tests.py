import unittest
import requests


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': 'OAuth '}

    def tearDown(self):
        # requests.delete(self.url, headers=self.headers, params={'path': '/test_folder'})
        del self.url
        del self.headers

    def test_create_folder_positive(self):
        params = {'path': 'test_folder'}

        response = requests.put(self.url, headers=self.headers, params=params)

        self.assertEqual(response.status_code, 201)

        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers=self.headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_create_folder_negative(self):
        params = {'path': '/test_folder'}

        response = requests.put(self.url, headers=self.headers, params=params)

        self.assertEqual(response.status_code, 409)

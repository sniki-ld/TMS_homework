import unittest
from task_02 import *


class TestFunc(unittest.TestCase):

    def setUp(self):
        self.url = 'https://cdn.pixabay.com/photo/2021/02/20/18/11/sea-6034191_1280.jpg'
        self.res = requests.get(self.url)

    def tearDown(self):
        pass

    def test_status_code(self):
        res = self.res.status_code
        self.assertTrue(200 <= res <= 299)
        self.assertFalse(400 <= res <= 599)


if __name__ == '__main':
    unittest.main()

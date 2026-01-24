import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_ludic(0), [])

    def test_single_element(self):
        self.assertEqual(get_ludic(1), [1])

    def test_small_list(self):
        self.assertEqual(get_ludic(3), [1, 2, 3])

    def test_large_list(self):
        self.assertEqual(get_ludic(10), [1, 3, 4, 7, 8, 10, 15, 16, 23, 24])

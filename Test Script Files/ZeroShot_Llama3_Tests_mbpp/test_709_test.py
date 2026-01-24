import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_get_unique(self):
        test_list = [['a', 1], ['b', 1], ['c', 2], ['d', 2], ['e', 3], ['f', 3]]
        self.assertEqual(get_unique(test_list), "{'1': 2, '2': 2, '3': 2}")

    def test_get_unique_empty(self):
        test_list = []
        self.assertEqual(get_unique(test_list), "{}")

    def test_get_unique_single(self):
        test_list = [['a', 1]]
        self.assertEqual(get_unique(test_list), "{'1': 1}")

    def test_get_unique_multiple(self):
        test_list = [['a', 1], ['b', 1], ['c', 2], ['d', 2], ['e', 3], ['f', 3], ['g', 1], ['h', 2]]
        self.assertEqual(get_unique(test_list), "{'1': 2, '2': 2, '3': 2}")

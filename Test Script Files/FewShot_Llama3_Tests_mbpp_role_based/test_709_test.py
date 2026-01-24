import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_single_element_list(self):
        test_list = [['a', 1]]
        self.assertEqual(get_unique(test_list), '{"1": 1}')

    def test_multiple_elements_list(self):
        test_list = [['a', 1], ['b', 1], ['c', 2]]
        self.assertEqual(get_unique(test_list), '{"1": 2, "2": 1}')

    def test_empty_list(self):
        test_list = []
        self.assertEqual(get_unique(test_list), '{}')

    def test_list_with_duplicates(self):
        test_list = [['a', 1], ['a', 1], ['b', 2], ['c', 2]]
        self.assertEqual(get_unique(test_list), '{"1": 1, "2": 1}')

    def test_list_with_empty_sublist(self):
        test_list = [['', 1], ['b', 2], ['c', 2]]
        self.assertEqual(get_unique(test_list), '{"1": 1, "2": 1}')

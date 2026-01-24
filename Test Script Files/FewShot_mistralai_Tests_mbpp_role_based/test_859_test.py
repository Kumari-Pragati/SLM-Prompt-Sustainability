import unittest
from mbpp_859_code import sub_lists

class TestSubLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sub_lists([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(sub_lists([1, 2, 3]), [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_negative_index(self):
        self.assertRaises(IndexError, sub_lists, [-1])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        self.assertEqual(len(sub_lists(large_list)), 103)

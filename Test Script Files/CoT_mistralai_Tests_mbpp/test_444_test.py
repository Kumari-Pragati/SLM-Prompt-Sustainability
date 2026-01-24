import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(trim_tuple([], 0), "[]")

    def test_single_element_list(self):
        self.assertEqual(trim_tuple([1, 2, 3], 1), "[]")
        self.assertEqual(trim_tuple([1], 0), "[]")

    def test_normal_list(self):
        self.assertEqual(trim_tuple([1, 2, 3, 4, 5], 2), "['3', '4']")
        self.assertEqual(trim_tuple([1, 2, 3, 4, 5], 1), "['2', '3', '4']")

    def test_list_with_odd_length(self):
        self.assertEqual(trim_tuple([1, 2, 3, 4], 2), "['3', '4']")

    def test_list_with_even_length(self):
        self.assertEqual(trim_tuple([1, 2, 3, 4], 1), "['2', '3']")

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            trim_tuple([1, 2, 3], -1)

    def test_index_larger_than_list_length(self):
        with self.assertRaises(IndexError):
            trim_tuple([1, 2, 3], 4)

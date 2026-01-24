import unittest
from mbpp_659_code import Repeat

class TestRepeatFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertListEqual(Repeat([1]), [1])

    def test_duplicate_elements(self):
        self.assertListEqual(Repeat([1, 1, 2, 2, 3]), [1, 2])

    def test_no_duplicates(self):
        self.assertListEqual(Repeat([1, 2, 3]), [])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            Repeat([1, 2, 3], -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            Repeat([1, 2, 3], 4)

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            Repeat(123)

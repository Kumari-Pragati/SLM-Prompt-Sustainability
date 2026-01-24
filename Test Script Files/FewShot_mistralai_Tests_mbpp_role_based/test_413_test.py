import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_valid_list_and_index(self):
        self.assertEqual(extract_nth_element([(1, 2), (3, 4), (5, 6)], 0), [1, 3, 5])
        self.assertEqual(extract_nth_element([(1, 2), (3, 4), (5, 6)], 1), [2, 4, 6])

    def test_empty_list(self):
        self.assertListEqual(extract_nth_element([], 0), [])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            extract_nth_element([(1, 2), (3, 4), (5, 6)], -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            extract_nth_element([(1, 2), (3, 4), (5, 6)], 2)

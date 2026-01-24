import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_rear([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(extract_rear([]), [])

    def test_single_list(self):
        self.assertEqual(extract_rear([[1]]), [1])

    def test_single_element_list(self):
        self.assertEqual(extract_rear([[1, 2]]), [2])

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_rear, [[-1]])

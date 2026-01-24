import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_rear([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_rear([1]), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_rear([1, 2, 3]), [3, 2, 1])

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_rear, [1, 2, 3], -1)

    def test_zero_index(self):
        self.assertRaises(IndexError, extract_rear, [1, 2, 3], 0)

    def test_list_with_non_list_element(self):
        self.assertRaises(TypeError, extract_rear, [1, 2, [3], 4])

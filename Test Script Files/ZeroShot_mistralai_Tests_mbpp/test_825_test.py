import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(access_elements([], []), [])

    def test_single_element(self):
        self.assertListEqual(access_elements([1], [0]), [1])

    def test_multiple_elements(self):
        self.assertListEqual(access_elements([1, 2, 3, 4, 5], [1, 3]), [2, 4])

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, access_elements, [1, 2, 3], [4])

    def test_negative_index(self):
        self.assertRaises(IndexError, access_elements, [1, 2, 3], [-1])

    def test_invalid_index_type(self):
        self.assertRaises(TypeError, access_elements, [1, 2, 3], [4.5])

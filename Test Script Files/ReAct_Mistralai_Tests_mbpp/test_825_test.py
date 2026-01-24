import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            access_elements([], [0])

    def test_single_element_list(self):
        self.assertEqual(access_elements([1], [0]), [1])

    def test_single_index_list(self):
        self.assertEqual(access_elements([1, 2, 3], [1]), [2])

    def test_multiple_elements_list(self):
        self.assertEqual(access_elements([1, 2, 3, 4], [1, 2]), [2, 3])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            access_elements([1, 2, 3], [-1])

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            access_elements([1, 2, 3], [3])

    def test_list_index_length_mismatch(self):
        with self.assertRaises(ValueError):
            access_elements([1, 2, 3], [0, 1, 2, 3, 4])

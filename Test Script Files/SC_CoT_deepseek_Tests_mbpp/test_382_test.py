import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_rotation_count([5, 6, 7, 8, 9, 10, 1, 2, 3, 4]), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(find_rotation_count([1]), -1)

    def test_edge_case_sorted_array(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_rotation_count([5, 5, 5, 1, 2, 3, 4, 5]), 3)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(IndexError):
            find_rotation_count([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            find_rotation_count("not a list")

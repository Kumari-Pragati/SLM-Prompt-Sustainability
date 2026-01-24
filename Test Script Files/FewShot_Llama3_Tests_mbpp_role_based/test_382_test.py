import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_typical_use_case(self):
        A = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(find_rotation_count(A), 6)

    def test_edge_case_empty_array(self):
        A = []
        self.assertEqual(find_rotation_count(A), -1)

    def test_edge_case_single_element_array(self):
        A = [1]
        self.assertEqual(find_rotation_count(A), -1)

    def test_edge_case_array_with_duplicates(self):
        A = [1, 2, 3, 2, 1]
        self.assertEqual(find_rotation_count(A), -1)

    def test_edge_case_array_with_duplicates_and_rotation(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(find_rotation_count(A), 9)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            find_rotation_count(123)

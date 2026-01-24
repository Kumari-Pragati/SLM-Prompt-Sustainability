import unittest
from mbpp_111_code import common_in_nested_lists

class TestCommonInNestedLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [3])

    def test_edge_case_empty_list(self):
        self.assertEqual(common_in_nested_lists([]), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(common_in_nested_lists([[1]]), [1])

    def test_corner_case_no_common_elements(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [4, 5, 6]]), [])

    def test_corner_case_all_elements_common(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [1, 2, 3]]), [1, 2, 3])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists(123)

    def test_invalid_input_nested_non_list(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists([1, 'a', [1, 2]])

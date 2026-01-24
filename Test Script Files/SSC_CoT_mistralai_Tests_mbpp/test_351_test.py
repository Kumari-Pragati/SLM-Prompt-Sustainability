import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(first_Element([1, 2, 3, 2, 1, 3], 6, 2), 1)
        self.assertEqual(first_Element([4, 4, 4, 4, 4], 5, 1), 4)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 3), 3)

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 0), -1)

    def test_invalid_input_type_arr(self):
        self.assertRaises(TypeError, first_Element, 'str', 3, 1)

    def test_invalid_input_type_n(self):
        self.assertRaises(TypeError, first_Element, [1, 2, 3], 'str', 1)

    def test_invalid_input_type_k(self):
        self.assertRaises(TypeError, first_Element, [1, 2, 3], 3, 'str')

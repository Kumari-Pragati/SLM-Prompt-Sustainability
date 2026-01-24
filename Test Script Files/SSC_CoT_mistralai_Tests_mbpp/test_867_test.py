import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)

    def test_edge_case_even_length(self):
        self.assertEqual(min_Num([1, 2, 3, 4], 4), 2)
        self.assertEqual(min_Num([2, 4, 6, 8], 4), 1)

    def test_edge_case_odd_length(self):
        self.assertEqual(min_Num([1, 2, 3, 4], 4), 2)
        self.assertEqual(min_Num([2, 4, 6, 8, 9], 5), 1)

    def test_boundary_case_empty(self):
        self.assertEqual(min_Num([], 0), None)

    def test_boundary_case_single_element(self):
        self.assertEqual(min_Num([1], 1), 2)
        self.assertEqual(min_Num([2], 1), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_Num('string', 1)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            min_Num([1, 2, 3], -1)

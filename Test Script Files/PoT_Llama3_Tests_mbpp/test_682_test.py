import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_edge_case_zero(self):
        self.assertEqual(mul_list([1, 2, 3], [0, 0, 0]), [0, 0, 0])

    def test_edge_case_single_element(self):
        self.assertEqual(mul_list([1], [2]), [2])
        self.assertEqual(mul_list([1], [0]), [0])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_list([], [1, 2, 3]), [])
        self.assertEqual(mul_list([1, 2, 3], []), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_list([1], []), [])
        self.assertEqual(mul_list([], [1]), [])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, 3], [4, -5, 6]), [-4, 10, 18])

    def test_edge_case_mixed_signs(self):
        self.assertEqual(mul_list([1, -2, 3], [4, -5, 6]), [4, -10, 18])

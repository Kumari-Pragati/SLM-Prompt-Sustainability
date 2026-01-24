import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_edge_case_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(mul_list([7], [8]), [56])

    def test_corner_case_zeroes(self):
        self.assertEqual(mul_list([0, 1, 2], [0, 3, 4]), [0, 0, 0])

    def test_exceptional_case_unequal_lengths(self):
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], [4, 5])

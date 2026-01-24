import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 1, 3, 2])

    def test_edge_case_with_zero(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_boundary_case_with_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, 0, 1]), [0, -1, 1, -2, -3])

    def test_corner_case_with_large_numbers(self):
        self.assertEqual(rearrange_numbs([1000, 2000, 0, 500]), [0, 500, 1000, 2000])

    def test_corner_case_with_small_numbers(self):
        self.assertEqual(rearrange_numbs([0.001, 0.002, 0.003]), [0.001, 0.003, 0.002])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            rearrange_numbs("1,2,3")

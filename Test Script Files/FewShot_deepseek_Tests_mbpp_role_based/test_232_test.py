import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_with_single_element(self):
        self.assertEqual(larg_nnum([1], 1), [1])

    def test_boundary_case_with_empty_list(self):
        self.assertEqual(larg_nnum([], 3), [])

    def test_boundary_case_with_n_equal_to_zero(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 0), [])

    def test_error_handling_with_invalid_input(self):
        with self.assertRaises(TypeError):
            larg_nnum("not a list", 3)

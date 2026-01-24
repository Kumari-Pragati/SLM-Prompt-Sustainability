import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_edge_case_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_boundary_case_single_element(self):
        self.assertTrue(odd_position([1]))

    def test_corner_case_all_even(self):
        self.assertFalse(odd_position([2, 4, 6]))

    def test_corner_case_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_corner_case_mixed_even_odd(self):
        self.assertFalse(odd_position([1, 2, 3]))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            odd_position([1, 'a', 3])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            odd_position(123)

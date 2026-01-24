import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_single_element(self):
        self.assertTrue(solve([1], 1))

    def test_edge_case_empty_list(self):
        self.assertFalse(solve([], 1))

    def test_edge_case_single_element_negative(self):
        self.assertFalse(solve([-1], 1))

    def test_edge_case_single_element_zero(self):
        self.assertTrue(solve([0], 1))

    def test_edge_case_single_element_max(self):
        self.assertTrue(solve([sys.maxsize], 1))

    def test_edge_case_single_element_min(self):
        self.assertTrue(solve([-sys.maxsize - 1], 1))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            solve([1, 2, 3, 'a'], 5)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            solve(1, 5)

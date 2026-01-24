import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_edge_case_zero(self):
        self.assertEqual(swap_numbers(0, 2), (2, 0))

    def test_edge_case_same_numbers(self):
        self.assertEqual(swap_numbers(2, 2), (2, 2))

    def test_boundary_case_negative(self):
        self.assertEqual(swap_numbers(-1, -2), ( -2, -1 ))

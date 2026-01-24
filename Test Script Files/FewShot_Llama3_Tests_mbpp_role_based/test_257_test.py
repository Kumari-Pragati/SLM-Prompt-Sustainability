import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_edge_case_a_equal_b(self):
        self.assertEqual(swap_numbers(1, 1), (1, 1))

    def test_edge_case_b_equal_a(self):
        self.assertEqual(swap_numbers(2, 2), (2, 2))

    def test_edge_case_a_greater_than_b(self):
        self.assertEqual(swap_numbers(3, 2), (2, 3))

    def test_edge_case_b_greater_than_a(self):
        self.assertEqual(swap_numbers(2, 3), (3, 2))

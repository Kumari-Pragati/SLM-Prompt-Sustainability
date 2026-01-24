import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(swap_numbers(5, 7), (7, 5))

    def test_edge_case_zero(self):
        self.assertEqual(swap_numbers(0, 7), (7, 0))

    def test_edge_case_negative(self):
        self.assertEqual(swap_numbers(-5, -7), (-7, -5))

    def test_edge_case_max_int(self):
        self.assertEqual(swap_numbers(2147483647, 1), (1, 2147483647))

    def test_edge_case_min_int(self):
        self.assertEqual(swap_numbers(-2147483648, -1), (-1, -2147483648))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            swap_numbers('a', 'b')

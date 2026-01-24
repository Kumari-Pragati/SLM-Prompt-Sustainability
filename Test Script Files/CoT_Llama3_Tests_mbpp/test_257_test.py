import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))
        self.assertEqual(swap_numbers(-1, 0), (0, -1))
        self.assertEqual(swap_numbers(0, 0), (0, 0))
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))
        self.assertEqual(swap_numbers(1, 1), (1, 1))

    def test_swap_numbers_edge_cases(self):
        self.assertEqual(swap_numbers(0, float('inf')), (float('inf'), 0))
        self.assertEqual(swap_numbers(float('-inf'), 0), (0, float('-inf')))

    def test_swap_numbers_invalid_inputs(self):
        with self.assertRaises(TypeError):
            swap_numbers('a', 2)
        with self.assertRaises(TypeError):
            swap_numbers(1, 'b')

import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_simple_swap(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))

    def test_swap_same_numbers(self):
        self.assertEqual(swap_numbers(2, 2), (2, 2))

    def test_min_max_values(self):
        self.assertEqual(swap_numbers(-100, 100), (100, -100))
        self.assertEqual(swap_numbers(sys.maxsize, sys.maxsize), (sys.maxsize, sys.maxsize))

    def test_edge_cases(self):
        self.assertEqual(swap_numbers(0, 1), (1, 0))
        self.assertEqual(swap_numbers(-1, 0), (0, -1))
        self.assertEqual(swap_numbers(sys.maxsize - 1, sys.maxsize), (sys.maxsize, sys.maxsize - 1))

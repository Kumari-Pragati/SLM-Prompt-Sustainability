import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))
        self.assertEqual(swap_numbers(0, 0), (0, 0))
        self.assertEqual(swap_numbers(-1, 1), (1, -1))
        self.assertEqual(swap_numbers('a', 'b'), ('b', 'a'))
        self.assertEqual(swap_numbers([1, 2, 3], [4, 5, 6]), ([4, 5, 6], [1, 2, 3]))

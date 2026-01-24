import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(1, 2), (2, 1))
        self.assertEqual(swap_numbers(3, 4), (4, 3))
        self.assertEqual(swap_numbers(5, 6), (6, 5))
        self.assertEqual(swap_numbers(0, 0), (0, 0))
        self.assertEqual(swap_numbers(-1, -2), (-2, -1))
        self.assertEqual(swap_numbers(float('nan'), float('nan')), (float('nan'), float('nan')))
        self.assertEqual(swap_numbers(True, False), (False, True))
        self.assertEqual(swap_numbers('a', 'b'), ('b', 'a'))
        self.assertEqual(swap_numbers(None, None), (None, None))

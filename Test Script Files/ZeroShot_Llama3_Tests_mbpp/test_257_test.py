import unittest
from mbpp_257_code import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(1,2), (2,1))
        self.assertEqual(swap_numbers(3,4), (4,3))
        self.assertEqual(swap_numbers(5,6), (6,5))
        self.assertEqual(swap_numbers(-1,-2), (-2,-1))
        self.assertEqual(swap_numbers(-3,-4), (-4,-3))
        self.assertEqual(swap_numbers(-5,-6), (-6,-5))

    def test_swap_numbers_with_negative_and_positive(self):
        self.assertEqual(swap_numbers(-1,2), (2,-1))
        self.assertEqual(swap_numbers(-3,4), (4,-3))
        self.assertEqual(swap_numbers(-5,6), (6,-5))

    def test_swap_numbers_with_zero(self):
        self.assertEqual(swap_numbers(0,1), (1,0))
        self.assertEqual(swap_numbers(0,2), (2,0))
        self.assertEqual(swap_numbers(0,-1), (-1,0))
        self.assertEqual(swap_numbers(0,-2), (-2,0))

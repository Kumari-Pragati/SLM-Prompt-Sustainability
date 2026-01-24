import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_multiply_num(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5]), -3.0)
        self.assertEqual(multiply_num([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5, -6]), -3.5)
        self.assertEqual(multiply_num([1, 2, 3, 4, 5, 6, 7]), 3.75)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5, -6, -7]), -3.75)
        self.assertEqual(multiply_num([1, 2, 3, 4, 5, 6, 7, 8]), 4.0)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5, -6, -7, -8]), -4.0)
        self.assertEqual(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9]), 4.5)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -4.5)
        self.assertEqual(multiply_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.0)
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -5.0)

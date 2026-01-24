import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_small_positive_input(self):
        self.assertEqual(odd_Num_Sum(3), 81)

    def test_large_positive_input(self):
        self.assertEqual(odd_Num_Sum(10), 14580)

    def test_zero_input(self):
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(3.5)

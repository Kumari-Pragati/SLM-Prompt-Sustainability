import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(5), 114916)

    def test_small_number(self):
        self.assertEqual(odd_Num_Sum(1), 1)

    def test_large_number(self):
        self.assertEqual(odd_Num_Sum(10), 1669245489)

    def test_zero(self):
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            odd_Num_Sum(-5)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            odd_Num_Sum(5.5)

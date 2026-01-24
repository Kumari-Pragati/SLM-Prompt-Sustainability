import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_one(self):
        self.assertEqual(odd_Num_Sum(1), 0)

    def test_small(self):
        self.assertEqual(odd_Num_Sum(5), 625)

    def test_large(self):
        self.assertEqual(odd_Num_Sum(10), 2850625)

    def test_negative(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(3.5)

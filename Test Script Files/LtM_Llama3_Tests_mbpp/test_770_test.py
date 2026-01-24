import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 9)
        self.assertEqual(odd_Num_Sum(3), 36)
        self.assertEqual(odd_Num_Sum(4), 81)
        self.assertEqual(odd_Num_Sum(5), 144)

    def test_edge(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(10), 2250)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')
        with self.assertRaises(TypeError):
            odd_Num_Sum(None)

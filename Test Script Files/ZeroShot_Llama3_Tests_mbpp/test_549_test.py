import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_Num_Sum(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 0)
        self.assertEqual(odd_Num_Sum(3), 225)
        self.assertEqual(odd_Num_Sum(4), 0)
        self.assertEqual(odd_Num_Sum(5), 1225)
        self.assertEqual(odd_Num_Sum(6), 0)
        self.assertEqual(odd_Num_Sum(7), 3375)
        self.assertEqual(odd_Num_Sum(8), 0)
        self.assertEqual(odd_Num_Sum(9), 9261)
        self.assertEqual(odd_Num_Sum(10), 0)

    def test_edge_cases(self):
        self.assertRaises(TypeError, odd_Num_Sum, 'a')
        self.assertRaises(TypeError, odd_Num_Sum, None)
        self.assertRaises(TypeError, odd_Num_Sum, [])

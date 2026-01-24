import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(3), 3)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(15), 41)
        self.assertEqual(sum_of_odd_Factors(21), 105)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(6), 6)
        self.assertEqual(sum_of_odd_Factors(7), 7)
        self.assertEqual(sum_of_odd_Factors(8), 8)
        self.assertEqual(sum_of_odd_Factors(9), 9)
        self.assertEqual(sum_of_odd_Factors(10), 25)
        self.assertEqual(sum_of_odd_Factors(11), 33)
        self.assertEqual(sum_of_odd_Factors(12), 24)
        self.assertEqual(sum_of_odd_Factors(13), 13)
        self.assertEqual(sum_of_odd_Factors(14), 14)
        self.assertEqual(sum_of_odd_Factors(16), 25)
        self.assertEqual(sum_of_odd_Factors(17), 17)
        self.assertEqual(sum_of_odd_Factors(18), 18)
        self.assertEqual(sum_of_odd_Factors(19), 19)
        self.assertEqual(sum_of_odd_Factors(20), 41)
        self.assertEqual(sum_of_odd_Factors(22), 41)
        self.assertEqual(sum_of_odd_Factors(23), 23)
        self.assertEqual(sum_of_odd_Factors(24), 24)
        self.assertEqual(sum_of_odd_Factors(25), 15)
        self.assertEqual(sum_of_odd_Factors(26), 26)
        self.assertEqual(sum_of_odd_Factors(27), 27)
        self.assertEqual(sum_of_odd_Factors(28), 28)
        self.assertEqual(sum_of_odd_Factors(29), 29)
        self.assertEqual(sum_of_odd_Factors(30), 63)
        self.assertEqual(sum_of_odd_Factors(31), 31)
        self.assertEqual(sum_of_odd_Factors(32), 32)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_of_odd_Factors, 0)
        self.assertRaises(TypeError, sum_of_odd_Factors, 'a')
        self.assertRaises(TypeError, sum_of_odd_Factors, 3.14)

import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_fourth_Power_Sum(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 30)
        self.assertEqual(fourth_Power_Sum(3), 105)
        self.assertEqual(fourth_Power_Sum(4), 280)
        self.assertEqual(fourth_Power_Sum(5), 635)
        self.assertEqual(fourth_Power_Sum(6), 1260)
        self.assertEqual(fourth_Power_Sum(7), 2255)
        self.assertEqual(fourth_Power_Sum(8), 3720)
        self.assertEqual(fourth_Power_Sum(9), 5775)
        self.assertEqual(fourth_Power_Sum(10), 8550)

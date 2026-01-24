import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_fifth_Power_Sum(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 32)
        self.assertEqual(fifth_Power_Sum(3), 288)
        self.assertEqual(fifth_Power_Sum(4), 2048)
        self.assertEqual(fifth_Power_Sum(5), 14400)
        self.assertEqual(fifth_Power_Sum(6), 77760)
        self.assertEqual(fifth_Power_Sum(7), 352800)
        self.assertEqual(fifth_Power_Sum(8), 1612800)
        self.assertEqual(fifth_Power_Sum(9), 7054320)
        self.assertEqual(fifth_Power_Sum(10), 24309000)

    def test_fifth_Power_Sum_edge_case(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

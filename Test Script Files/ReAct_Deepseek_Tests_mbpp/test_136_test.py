import unittest
from mbpp_136_code import cal_electbill

class TestElectBillCalculator(unittest.TestCase):

    def test_less_than_50_units(self):
        self.assertEqual(cal_electbill(20), 52)
        self.assertEqual(cal_electbill(49), 129.4)

    def test_50_to_100_units(self):
        self.assertEqual(cal_electbill(50), 130)
        self.assertEqual(cal_electbill(75), 218.75)
        self.assertEqual(cal_electbill(100), 355)

    def test_100_to_200_units(self):
        self.assertEqual(cal_electbill(101), 562.55)
        self.assertEqual(cal_electbill(150), 1012.5)
        self.assertEqual(cal_electbill(200), 2035)

    def test_more_than_200_units(self):
        self.assertEqual(cal_electbill(201), 2877.45)
        self.assertEqual(cal_electbill(300), 5035)

    def test_negative_units(self):
        with self.assertRaises(Exception):
            cal_electbill(-10)

    def test_zero_units(self):
        self.assertEqual(cal_electbill(0), 25)

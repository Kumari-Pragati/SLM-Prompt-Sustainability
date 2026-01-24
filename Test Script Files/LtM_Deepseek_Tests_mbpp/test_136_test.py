import unittest
from mbpp_136_code import cal_electbill

class TestElectBill(unittest.TestCase):

    def test_less_than_50_units(self):
        self.assertEqual(cal_electbill(25), 65)
        self.assertEqual(cal_electbill(49), 125.4)

    def test_50_to_100_units(self):
        self.assertEqual(cal_electbill(50), 130)
        self.assertEqual(cal_electbill(99), 349.5)

    def test_100_to_200_units(self):
        self.assertEqual(cal_electbill(100), 462.5)
        self.assertEqual(cal_electbill(199), 2034.5)

    def test_more_than_200_units(self):
        self.assertEqual(cal_electbill(200), 2076)
        self.assertEqual(cal_electbill(300), 3267)

    def test_negative_units(self):
        self.assertEqual(cal_electbill(-10), 0)

    def test_zero_units(self):
        self.assertEqual(cal_electbill(0), 25)

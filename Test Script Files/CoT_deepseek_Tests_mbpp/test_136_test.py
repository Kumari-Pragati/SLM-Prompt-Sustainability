import unittest
from mbpp_136_code import cal_electbill

class TestElectBill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(25), 65)
        self.assertEqual(cal_electbill(49), 117.4)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 301.25)
        self.assertEqual(cal_electbill(99), 431.75)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 1130.5)
        self.assertEqual(cal_electbill(199), 1657.75)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 2130.5)
        self.assertEqual(cal_electbill(300), 3302.5)

    def test_units_less_than_0(self):
        with self.assertRaises(Exception):
            cal_electbill(-10)

    def test_units_equal_to_0(self):
        self.assertEqual(cal_electbill(0), 25)

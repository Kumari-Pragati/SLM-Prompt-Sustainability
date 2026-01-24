import unittest
from mbpp_136_code import cal_electbill

class TestCalElectBill(unittest.TestCase):
    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(40), 104)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 280)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 562.5)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 1300 + 526 + 1275)

    def test_units_more_than_200_and_less_than_300(self):
        self.assertEqual(cal_electbill(299), 1300 + 526 + 1275 + 253.5)

    def test_units_less_than_0(self):
        with self.assertRaises(ValueError):
            cal_electbill(-10)

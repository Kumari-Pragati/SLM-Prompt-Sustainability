import unittest
from mbpp_136_code import cal_electbill

class TestCalElectBill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(40), 104)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 230)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 472.5)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 1082.5)

    def test_units_exceeding_400(self):
        self.assertEqual(cal_electbill(450), 2182.5)

    def test_negative_units(self):
        self.assertRaises(ValueError, cal_electbill, -10)

    def test_zero_units(self):
        self.assertEqual(cal_electbill(0), 130)

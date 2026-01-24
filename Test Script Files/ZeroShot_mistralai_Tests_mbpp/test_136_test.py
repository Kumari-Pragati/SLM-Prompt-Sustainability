import unittest
from mbpp_136_code import cal_electbill

class TestCalElectBill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(20), 52.0)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 231.25)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 457.5)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 1023.75)

    def test_surcharge_calculation(self):
        self.assertEqual(cal_electbill(249), 1023.75)
        self.assertEqual(cal_electbill(251), 1078.15)

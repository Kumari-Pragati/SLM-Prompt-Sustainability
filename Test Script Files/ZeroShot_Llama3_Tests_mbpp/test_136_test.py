import unittest
from mbpp_136_code import cal_electbill

class TestCalElectBill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(49), 123.00)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 195.00)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 417.75)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 933.75)

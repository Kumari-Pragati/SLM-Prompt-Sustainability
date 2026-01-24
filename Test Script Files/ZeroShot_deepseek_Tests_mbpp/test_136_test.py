import unittest
from mbpp_136_code import cal_electbill

class TestElectBill(unittest.TestCase):

    def test_cal_electbill_less_than_50(self):
        self.assertEqual(cal_electbill(20), 52)

    def test_cal_electbill_50_to_100(self):
        self.assertEqual(cal_electbill(75), 213.75)

    def test_cal_electbill_100_to_200(self):
        self.assertEqual(cal_electbill(150), 463.75)

    def test_cal_electbill_more_than_200(self):
        self.assertEqual(cal_electbill(250), 1063.75)

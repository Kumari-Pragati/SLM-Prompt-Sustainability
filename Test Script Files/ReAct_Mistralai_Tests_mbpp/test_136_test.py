import unittest
from mbpp_136_code import cal_electbill

class TestElectricBill(unittest.TestCase):

    def test_units_below_50(self):
        self.assertEqual(cal_electbill(40), 104.0)

    def test_units_exactly_50(self):
        self.assertEqual(cal_electbill(50), 130.0)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 237.5)

    def test_units_exactly_100(self):
        self.assertEqual(cal_electbill(100), 130.0 + 35.0)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 427.5)

    def test_units_exactly_200(self):
        self.assertEqual(cal_electbill(200), 472.5)

    def test_units_above_200(self):
        self.assertEqual(cal_electbill(250), 130.0 + 162.50 + 526.0 + 1087.5)

    def test_units_at_boundary_cases(self):
        self.assertEqual(cal_electbill(49), 130.0 + 24.7)
        self.assertEqual(cal_electbill(99), 130.0 + 35.0 + 132.5)
        self.assertEqual(cal_electbill(199), 472.5 + 168.45)
        self.assertEqual(cal_electbill(201), 472.5 + 168.45 + 8.45)

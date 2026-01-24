import unittest
from mbpp_136_code import cal_electbill

class TestCalElectbill(unittest.TestCase):
    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(49), 123.50)
        self.assertEqual(cal_electbill(0), 25)
        self.assertEqual(cal_electbill(-1), 25)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(50), 130)
        self.assertEqual(cal_electbill(75), 195.00)
        self.assertEqual(cal_electbill(100), 195.00)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(101), 195.00 + 5.26)
        self.assertEqual(cal_electbill(150), 195.00 + 162.50 + 5.26)
        self.assertEqual(cal_electbill(200), 195.00 + 162.50 + 526.00)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(201), 195.00 + 162.50 + 526.00 + 8.45)
        self.assertEqual(cal_electbill(250), 195.00 + 162.50 + 526.00 + 8.45 * 50)

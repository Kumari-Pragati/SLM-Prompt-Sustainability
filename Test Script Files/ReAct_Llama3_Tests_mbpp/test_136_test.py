import unittest
from mbpp_136_code import cal_electbill

class TestCalElectbill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(49), 123.90)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(75), 195.75)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 417.75)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 817.75)

    def test_units_zero(self):
        self.assertEqual(cal_electbill(0), 25)

    def test_units_negative(self):
        with self.assertRaises(TypeError):
            cal_electbill(-1)

import unittest
from mbpp_136_code import cal_electbill

class TestCalElectbill(unittest.TestCase):
    def test_low_usage(self):
        self.assertEqual(cal_electbill(20), 65.0)

    def test_medium_usage(self):
        self.assertEqual(cal_electbill(80), 235.0)

    def test_high_usage(self):
        self.assertEqual(cal_electbill(220), 647.75)

    def test_extreme_usage(self):
        self.assertEqual(cal_electbill(250), 1073.75)

    def test_zero_usage(self):
        self.assertEqual(cal_electbill(0), 25)

    def test_negative_usage(self):
        with self.assertRaises(TypeError):
            cal_electbill(-10)

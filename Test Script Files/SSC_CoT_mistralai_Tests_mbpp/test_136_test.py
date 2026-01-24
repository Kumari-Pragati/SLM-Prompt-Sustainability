import unittest
from mbpp_136_code import cal_electbill

class TestElectricBill(unittest.TestCase):

    def test_normal_usage(self):
        self.assertEqual(cal_electbill(50), 130 + 25)
        self.assertEqual(cal_electbill(100), 130 + 130 + 35)
        self.assertEqual(cal_electbill(200), 130 + 162.50 + 45)

    def test_edge_cases(self):
        self.assertEqual(cal_electbill(49), 130 + 25)
        self.assertEqual(cal_electbill(101), 130 + 130 + 35)
        self.assertEqual(cal_electbill(201), 130 + 162.50 + 45 + 5.26)
        self.assertEqual(cal_electbill(299), 130 + 162.50 + 526 + 75)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            cal_electbill(-10)
        with self.assertRaises(ValueError):
            cal_electbill(301)

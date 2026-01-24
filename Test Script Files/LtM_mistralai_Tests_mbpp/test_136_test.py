import unittest
from mbpp_136_code import cal_electbill

class TestElectricBill(unittest.TestCase):

    def test_simple_units(self):
        self.assertEqual(cal_electbill(25), 65)
        self.assertEqual(cal_electbill(50), 130)
        self.assertEqual(cal_electbill(100), 195)
        self.assertEqual(cal_electbill(150), 387.5)

    def test_edge_units(self):
        self.assertEqual(cal_electbill(49), 130 + 25)
        self.assertEqual(cal_electbill(101), 195 + 35)
        self.assertEqual(cal_electbill(201), 627.5)
        self.assertEqual(cal_electbill(201.01), 627.5845)
        self.assertEqual(cal_electbill(299), 130 + 162.5 + 526 + 75)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, cal_electbill, -10)
        self.assertRaises(ValueError, cal_electbill, 201.001)

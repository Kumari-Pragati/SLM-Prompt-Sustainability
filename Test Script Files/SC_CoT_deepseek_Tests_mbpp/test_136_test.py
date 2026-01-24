import unittest
from mbpp_136_code import cal_electbill

class TestElectricityBill(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(cal_electbill(75), 215.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(cal_electbill(50), 130.0)
        self.assertAlmostEqual(cal_electbill(100), 262.5)
        self.assertAlmostEqual(cal_electbill(200), 1062.5)

    def test_edge_case(self):
        self.assertAlmostEqual(cal_electbill(0), 130.0)
        self.assertAlmostEqual(cal_electbill(51), 162.5)
        self.assertAlmostEqual(cal_electbill(101), 526.5)
        self.assertAlmostEqual(cal_electbill(201), 3466.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cal_electbill('50')
        with self.assertRaises(ValueError):
            cal_electbill(-50)

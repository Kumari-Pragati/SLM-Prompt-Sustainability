import unittest
from mbpp_136_code import cal_electbill

class TestElectBill(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(cal_electbill(75), 216.25, places=2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(cal_electbill(50), 130.00, places=2)
        self.assertAlmostEqual(cal_electbill(100), 212.50, places=2)
        self.assertAlmostEqual(cal_electbill(200), 526.50, places=2)

    def test_edge_conditions(self):
        self.assertAlmostEqual(cal_electbill(0), 130.00, places=2)
        self.assertAlmostEqual(cal_electbill(300), 130.00 + 162.50 + 526.00 + 336.75, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cal_electbill('50')
        with self.assertRaises(ValueError):
            cal_electbill(-10)

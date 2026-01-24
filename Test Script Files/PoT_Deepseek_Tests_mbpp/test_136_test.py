import unittest
from mbpp_136_code import cal_electbill

class TestElectBill(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(cal_electbill(30), 81.8, places=2)
        self.assertAlmostEqual(cal_electbill(100), 355.0, places=2)
        self.assertAlmostEqual(cal_electbill(200), 1162.5, places=2)
        self.assertAlmostEqual(cal_electbill(300), 2035.0, places=2)

    def test_edge_cases(self):
        self.assertAlmostEqual(cal_electbill(0), 50, places=2)
        self.assertAlmostEqual(cal_electbill(50), 130, places=2)
        self.assertAlmostEqual(cal_electbill(100), 355.0, places=2)
        self.assertAlmostEqual(cal_electbill(200), 1162.5, places=2)

    def test_boundary_cases(self):
        self.assertAlmostEqual(cal_electbill(50), 130, places=2)
        self.assertAlmostEqual(cal_electbill(100), 355.0, places=2)
        self.assertAlmostEqual(cal_electbill(200), 1162.5, places=2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cal_electbill('invalid')
        with self.assertRaises(ValueError):
            cal_electbill(-10)

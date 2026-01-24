import unittest
from mbpp_136_code import cal_electbill

class TestCalElectBill(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cal_electbill(40), 104.0)
        self.assertEqual(cal_electbill(101), 165.0)
        self.assertEqual(cal_electbill(199), 467.0)
        self.assertEqual(cal_electbill(201), 542.45)
        self.assertEqual(cal_electbill(250), 797.45)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(cal_electbill(0), 25.0)
        self.assertEqual(cal_electbill(49), 130.0)
        self.assertEqual(cal_electbill(51), 133.25)
        self.assertEqual(cal_electbill(101.001), 165.0)
        self.assertEqual(cal_electbill(199.999), 467.0)
        self.assertEqual(cal_electbill(200.001), 542.45)
        self.assertEqual(cal_electbill(250.001), 797.45)

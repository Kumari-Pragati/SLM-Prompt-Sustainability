import unittest
from mbpp_136_code import cal_electbill

class TestCalElectbill(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cal_electbill(0), 25)
        self.assertEqual(cal_electbill(50), 125)
        self.assertEqual(cal_electbill(100), 235)
        self.assertEqual(cal_electbill(200), 635)

    def test_edge(self):
        self.assertEqual(cal_electbill(49), 99)
        self.assertEqual(cal_electbill(50), 125)
        self.assertEqual(cal_electbill(100), 235)
        self.assertEqual(cal_electbill(200), 635)
        self.assertEqual(cal_electbill(201), 1065)

    def test_complex(self):
        self.assertEqual(cal_electbill(250), 1065)
        self.assertEqual(cal_electbill(300), 1415)
        self.assertEqual(cal_electbill(400), 1935)

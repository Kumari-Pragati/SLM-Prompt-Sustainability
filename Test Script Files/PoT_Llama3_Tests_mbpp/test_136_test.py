import unittest
from mbpp_136_code import cal_electbill

class TestCalElectbill(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cal_electbill(50), 125)
        self.assertEqual(cal_electbill(100), 235)
        self.assertEqual(cal_electbill(200), 525)

    def test_edge_case(self):
        self.assertEqual(cal_electbill(49), 127.8)
        self.assertEqual(cal_electbill(200), 525)
        self.assertEqual(cal_electbill(201), 675.45)

    def test_corner_case(self):
        self.assertEqual(cal_electbill(0), 25)
        self.assertEqual(cal_electbill(50), 125)
        self.assertEqual(cal_electbill(200), 525)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cal_electbill('a')

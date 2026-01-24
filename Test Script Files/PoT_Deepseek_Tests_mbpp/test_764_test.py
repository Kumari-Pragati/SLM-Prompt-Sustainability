import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(number_ctr("123abc456"), 6)
        self.assertEqual(number_ctr("abc"), 0)
        self.assertEqual(number_ctr("1234567890"), 10)

    def test_edge_cases(self):
        self.assertEqual(number_ctr(""), 0)
        self.assertEqual(number_ctr("0"), 1)
        self.assertEqual(number_ctr("a0b1c2d3e4f5"), 5)

    def test_corner_cases(self):
        self.assertEqual(number_ctr("0123456789"), 10)
        self.assertEqual(number_ctr("9876543210"), 10)

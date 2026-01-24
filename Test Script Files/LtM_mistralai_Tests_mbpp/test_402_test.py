import unittest
from mbpp_402_code import ncr_modp

class TestNCRModP(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(ncr_modp(2, 1, 3), 1)
        self.assertEqual(ncr_modp(3, 2, 5), 2)
        self.assertEqual(ncr_modp(4, 3, 7), 4)

    def test_edge_and_boundary(self):
        self.assertEqual(ncr_modp(0, 0, 2), 1)
        self.assertEqual(ncr_modp(1, 0, 2), 1)
        self.assertEqual(ncr_modp(1, 1, 2), 1)
        self.assertEqual(ncr_modp(100, 100, 101), 1)
        self.assertEqual(ncr_modp(100, 101, 101), 0)

    def test_complex(self):
        self.assertEqual(ncr_modp(10, 5, 7), 21)
        self.assertEqual(ncr_modp(20, 10, 13), 121)
        self.assertEqual(ncr_modp(50, 40, 59), 1)

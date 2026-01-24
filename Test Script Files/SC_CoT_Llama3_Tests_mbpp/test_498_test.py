import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_typical(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_gcd_edge(self):
        self.assertEqual(gcd(0, 0), 1)

    def test_gcd_edge2(self):
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_edge3(self):
        self.assertEqual(gcd(1, 0), 1)

    def test_gcd_edge4(self):
        self.assertEqual(gcd(0, 1), 1)

    def test_gcd_edge5(self):
        self.assertEqual(gcd(2, 3), 1)

    def test_gcd_edge6(self):
        self.assertEqual(gcd(3, 2), 1)

    def test_gcd_edge7(self):
        self.assertEqual(gcd(4, 6), 2)

    def test_gcd_edge8(self):
        self.assertEqual(gcd(6, 4), 2)

    def test_gcd_edge9(self):
        self.assertEqual(gcd(10, 15), 5)

    def test_gcd_edge10(self):
        self.assertEqual(gcd(15, 10), 5)

    def test_gcd_edge11(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_edge12(self):
        self.assertEqual(gcd(18, 48), 6)

    def test_gcd_edge13(self):
        self.assertEqual(gcd(36, 54), 18)

    def test_gcd_edge14(self):
        self.assertEqual(gcd(54, 36), 18)

    def test_gcd_edge15(self):
        self.assertEqual(gcd(72, 108), 36)

    def test_gcd_edge16(self):
        self.assertEqual(gcd(108, 72), 36)

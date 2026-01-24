import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_typical(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_gcd_edge1(self):
        self.assertEqual(gcd(10, 5), 5)

    def test_gcd_edge2(self):
        self.assertEqual(gcd(15, 15), 15)

    def test_gcd_edge3(self):
        self.assertEqual(gcd(24, 30), 6)

    def test_gcd_edge4(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_edge5(self):
        self.assertEqual(gcd(36, 12), 12)

    def test_gcd_edge6(self):
        self.assertEqual(gcd(18, 24), 6)

    def test_gcd_edge7(self):
        self.assertEqual(gcd(24, 48), 12)

    def test_gcd_edge8(self):
        self.assertEqual(gcd(12, 24), 12)

    def test_gcd_edge9(self):
        self.assertEqual(gcd(15, 24), 3)

    def test_gcd_edge10(self):
        self.assertEqual(gcd(24, 15), 3)

    def test_gcd_edge11(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge12(self):
        self.assertEqual(gcd(24, 24), 24)

    def test_gcd_edge13(self):
        self.assertEqual(gcd(12, 0), 12)

    def test_gcd_edge14(self):
        self.assertEqual(gcd(0, 12), 12)

    def test_gcd_edge15(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge16(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge17(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge18(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge19(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_edge20(self):
        self.assertEqual(gcd(12, 12), 12)

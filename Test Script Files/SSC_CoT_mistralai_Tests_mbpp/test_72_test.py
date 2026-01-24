import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_input(self):
        self.assertFalse(dif_Square(10))
        self.assertFalse(difi_Square(14))
        self.assertFalse(difi_Square(22))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(difi_Square(2))
        self.assertTrue(difi_Square(6))
        self.assertFalse(difi_Square(0))
        self.assertFalse(difi_Square(-2))
        self.assertFalse(difi_Square(3))
        self.assertFalse(difi_Square(4))
        self.assertFalse(difi_Square(5))
        self.assertFalse(difi_Square(7))
        self.assertFalse(difi_Square(8))
        self.assertFalse(difi_Square(9))
        self.assertFalse(difi_Square(11))
        self.assertFalse(difi_Square(12))
        self.assertFalse(difi_Square(13))
        self.assertFalse(difi_Square(15))
        self.assertFalse(difi_Square(16))
        self.assertFalse(difi_Square(17))
        self.assertFalse(difi_Square(18))
        self.assertFalse(difi_Square(19))
        self.assertFalse(difi_Square(20))
        self.assertFalse(difi_Square(21))
        self.assertFalse(difi_Square(23))
        self.assertFalse(difi_Square(24))
        self.assertFalse(difi_Square(25))
        self.assertFalse(difi_Square(26))
        self.assertFalse(difi_Square(28))
        self.assertFalse(difi_Square(30))

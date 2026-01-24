import unittest
from mbpp_683_code import range

class TestSumSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(sum_Square(4))
        self.assertTrue(sum_Square(9))
        self.assertTrue(sum_Square(16))
        self.assertTrue(sum_Square(25))
        self.assertTrue(sum_Square(36))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertFalse(sum_Square(2))
        self.assertTrue(sum_Square(3))
        self.assertFalse(sum_Square(49))
        self.assertFalse(sum_Square(50))
        self.assertFalse(sum_Square(62))
        self.assertTrue(sum_Square(64))
        self.assertFalse(sum_Square(81))
        self.assertFalse(sum_Square(121))
        self.assertFalse(sum_Square(144))
        self.assertTrue(sum_Square(169))
        self.assertFalse(sum_Square(225))
        self.assertFalse(sum_Square(256))

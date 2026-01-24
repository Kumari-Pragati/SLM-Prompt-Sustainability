import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_get_carol_positive(self):
        self.assertEqual(get_carol(0), 1)
        self.assertEqual(get_carol(1), 5)
        self.assertEqual(get_carol(2), 41)
        self.assertEqual(get_carol(3), 257)
        self.assertEqual(get_carol(4), 1681)

    def test_get_carol_negative(self):
        self.assertEqual(get_carol(-1), -3)
        self.assertEqual(get_carol(-2), 65)
        self.assertEqual(get_carol(-3), 4095)
        self.assertEqual(get_carol(-4), 262143)

    def test_get_carol_zero(self):
        self.assertRaises(ValueError, get_carol, 0)

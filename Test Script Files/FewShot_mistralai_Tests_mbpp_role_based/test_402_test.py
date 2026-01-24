import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(ncr_modp(5, 2, 3), 2)
        self.assertEqual(ncr_modp(10, 3, 5), 2)
        self.assertEqual(ncr_modp(20, 10, 7), 6)

    def test_zero_input(self):
        self.assertEqual(ncr_modp(0, 0, 7), 1)
        self.assertEqual(ncr_modp(0, 1, 7), 0)
        self.assertEqual(ncr_modp(0, 10, 7), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, ncr_modp, -1, 2, 3)
        self.assertRaises(ValueError, ncr_modp, 1, -2, 3)
        self.assertRaises(ValueError, ncr_modp, 1, 2, -3)

    def test_large_input(self):
        self.assertRaises(ValueError, ncr_modp, 1000000, 1000000, 10)
        self.assertRaises(ValueError, ncr_modp, 1000000, 1000001, 10)
        self.assertRaises(ValueError, ncr_modp, 1000001, 1000000, 10)

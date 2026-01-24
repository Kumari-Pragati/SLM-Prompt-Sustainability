import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_ncr_modp(self):
        self.assertEqual(ncr_modp(5, 2, 13), 10)
        self.assertEqual(ncr_modp(10, 5, 23), 10)
        self.assertEqual(ncr_modp(15, 10, 37), 26)
        self.assertEqual(ncr_modp(20, 15, 47), 36)
        self.assertEqual(ncr_modp(25, 20, 59), 52)

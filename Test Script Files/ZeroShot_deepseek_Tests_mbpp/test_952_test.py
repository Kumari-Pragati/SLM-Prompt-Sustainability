import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_nCr_mod_p(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 6)
        self.assertEqual(nCr_mod_p(10, 5, 23), 10)
        self.assertEqual(nCr_mod_p(15, 10, 37), 26)
        self.assertEqual(nCr_mod_p(20, 15, 47), 40)
        self.assertEqual(nCr_mod_p(25, 20, 59), 54)

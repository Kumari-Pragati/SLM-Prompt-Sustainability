import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):

    def test_nCr_mod_p(self):
        self.assertEqual(nCr_mod_p(5, 2, 7), 6)
        self.assertEqual(nCr_mod_p(10, 3, 11), 40)
        self.assertEqual(nCr_mod_p(20, 10, 13), 148)
        self.assertEqual(nCr_mod_p(5, 1, 7), 5)
        self.assertEqual(nCr_mod_p(10, 5, 11), 42)
        self.assertEqual(nCr_mod_p(20, 15, 13), 120)
        self.assertEqual(nCr_mod_p(5, 0, 7), 1)
        self.assertEqual(nCr_mod_p(10, 0, 11), 1)
        self.assertEqual(nCr_mod_p(20, 0, 13), 1)
        self.assertEqual(nCr_mod_p(5, 5, 7), 1)
        self.assertEqual(nCr_mod_p(10, 10, 11), 1)
        self.assertEqual(nCr_mod_p(20, 20, 13), 1)

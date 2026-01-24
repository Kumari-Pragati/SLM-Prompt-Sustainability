import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_nCr_mod_p(self):
        self.assertEqual(nCr_mod_p(2, 1, 5), 2)
        self.assertEqual(nCr_mod_p(2, 2, 5), 1)
        self.assertEqual(nCr_mod_p(3, 1, 5), 3)
        self.assertEqual(nCr_mod_p(3, 2, 5), 3)
        self.assertEqual(nCr_mod_p(3, 3, 5), 1)
        self.assertEqual(nCr_mod_p(4, 1, 5), 4)
        self.assertEqual(nCr_mod_p(4, 2, 5), 6)
        self.assertEqual(nCr_mod_p(4, 3, 5), 4)
        self.assertEqual(nCr_mod_p(4, 4, 5), 1)
        self.assertEqual(nCr_mod_p(5, 1, 5), 5)
        self.assertEqual(nCr_mod_p(5, 2, 5), 10)
        self.assertEqual(nCr_mod_p(5, 3, 5), 10)
        self.assertEqual(nCr_mod_p(5, 4, 5), 5)
        self.assertEqual(nCr_mod_p(5, 5, 5), 1)

        self.assertEqual(nCr_mod_p(10, 1, 10), 10)
        self.assertEqual(nCr_mod_p(10, 2, 10), 45)
        self.assertEqual(nCr_mod_p(10, 3, 10), 120)
        self.assertEqual(nCr_mod_p(10, 4, 10), 210)
        self.assertEqual(nCr_mod_p(10, 5, 10), 252)
        self.assertEqual(nCr_mod_p(10, 6, 10), 210)
        self.assertEqual(nCr_mod_p(10, 7, 10), 120)
        self.assertEqual(nCr_mod_p(10, 8, 10), 45)
        self.assertEqual(nCr_mod_p(10, 9, 10), 10)
        self.assertEqual(nCr_mod_p(10, 10, 10), 1)

        self.assertEqual(nCr_mod_p(100, 1, 10), 100)
        self.assertEqual(nCr_mod_p(100, 2, 10), 4950)
        self.assertEqual(nCr_mod_p(100, 3, 10), 19950)
        self.assertEqual(nCr_mod_p(100, 4, 10), 66090)
        self.assertEqual(nCr_mod_p(100, 5, 10), 169340)
        self.assertEqual(nCr_mod_p(100, 6, 10), 332650)
        self.assertEqual(nCr_mod_p(100, 7, 10), 505990)
        self.assertEqual(nCr_mod_p(100, 8, 10), 660900)
        self.assertEqual(nCr_mod_p(100, 9, 10), 660900)
        self.assertEqual(nCr_mod_p(100, 10, 10), 505990)

import unittest
from714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_count_fac_basic(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 2)
        self.assertEqual(count_Fac(10), 4)

    def test_count_fac_large_numbers(self):
        self.assertEqual(count_Fac(100), 164)
        self.assertEqual(count_Fac(1000), 1641)
        self.assertEqual(count_Fac(10000), 16417)
        self.assertEqual(count_Fac(100000), 164176)
        self.assertEqual(count_Fac(1000000), 1641765)

    def test_count_fac_prime(self):
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(11), 1)
        self.assertEqual(count_Fac(13), 1)
        self.assertEqual(count_Fac(17), 2)
        self.assertEqual(count_Fac(19), 1)
        self.assertEqual(count_Fac(23), 1)
        self.assertEqual(count_Fac(29), 2)

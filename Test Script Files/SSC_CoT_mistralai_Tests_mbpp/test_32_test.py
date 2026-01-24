import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_Prime_Factors(28), 7)
        self.assertEqual(max_Prime_Factors(496), 7)
        self.assertEqual(max_Prime_Factors(600800), 23)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_Prime_Factors(1), 1)
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(5), 5)
        self.assertEqual(max_Prime_Factors(6), 3)
        self.assertEqual(max_Prime_Factors(7), 7)
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_Prime_Factors(9), 3)
        self.assertEqual(max_Prime_Factors(10), 5)
        self.assertEqual(max_Prime_Factors(11), 11)
        self.assertEqual(max_Prime_Factors(12), 7)
        self.assertEqual(max_Prime_Factors(13), 13)
        self.assertEqual(max_Prime_Factors(14), 2)
        self.assertEqual(max_Prime_Factors(15), 5)
        self.assertEqual(max_Prime_Factors(16), 2)
        self.assertEqual(max_Prime_Factors(17), 17)
        self.assertEqual(max_Prime_Factors(18), 2)
        self.assertEqual(max_Prime_Factors(19), 19)
        self.assertEqual(max_Prime_Factors(20), 5)
        self.assertEqual(max_Prime_Factors(21), 7)
        self.assertEqual(max_Prime_Factors(22), 2)
        self.assertEqual(max_Prime_Factors(23), 23)
        self.assertEqual(max_Prime_Factors(24), 2)
        self.assertEqual(max_Prime_Factors(25), 5)
        self.assertEqual(max_Prime_Factors(26), 2)
        self.assertEqual(max_Prime_Factors(27), 3)
        self.assertEqual(max_Prime_Factors(28), 7)
        self.assertEqual(max_Prime_Factors(29), 29)
        self.assertEqual(max_Prime_Factors(30), 2)
        self.assertEqual(max_Prime_Factors(31), 31)

    def test_special_cases(self):
        self.assertEqual(max_Prime_Factors(123456789), 73)
        self.assertEqual(max_Prime_Factors(1234567890), 17)
        self.assertEqual(max_Prime_Factors(12345678901), 13)
        self.assertEqual(max_Prime_Factors(123456789012), 19)
        self.assertEqual(max_Prime_Factors(1234567890123), 23)
        self.assertEqual(max_Prime_Factors(12345678901234), 31)
        self.assertEqual(max_Prime_Factors(123456789012345), 37)
        self.assertEqual(max_Prime_Factors(1234567890123456), 41)
        self.assertEqual(max_Prime_
import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(100), 2)
        self.assertEqual(find_Digits(1000), 3)
        self.assertEqual(find_Digits(10000), 4)

    def test_edge_cases(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(-1), 0)
        self.assertEqual(find_Digits(2), 1)
        self.assertEqual(find_Digits(3), 2)

    def test_corner_cases(self):
        self.assertEqual(find_Digits(5), 2)
        self.assertEqual(find_Digits(7), 2)
        self.assertEqual(find_Digits(11), 2)
        self.assertEqual(find_Digits(12), 3)

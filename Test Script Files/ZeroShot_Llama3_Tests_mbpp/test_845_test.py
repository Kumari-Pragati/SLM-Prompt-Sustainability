import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_zero(self):
        self.assertEqual(find_Digits(0), 1)

    def test_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_small_numbers(self):
        self.assertEqual(find_Digits(2), 2)
        self.assertEqual(find_Digits(3), 2)
        self.assertEqual(find_Digits(4), 3)
        self.assertEqual(find_Digits(5), 3)
        self.assertEqual(find_Digits(6), 4)
        self.assertEqual(find_Digits(7), 4)
        self.assertEqual(find_Digits(8), 5)
        self.assertEqual(find_Digits(9), 5)

    def test_large_numbers(self):
        self.assertEqual(find_Digits(10), 5)
        self.assertEqual(find_Digits(100), 7)
        self.assertEqual(find_Digits(1000), 9)
        self.assertEqual(find_Digits(10000), 10)
        self.assertEqual(find_Digits(100000), 11)

    def test_edge_cases(self):
        self.assertEqual(find_Digits(math.inf), 1)
        self.assertEqual(find_Digits(-math.inf), 0)

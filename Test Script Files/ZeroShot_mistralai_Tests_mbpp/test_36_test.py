import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_find_Nth_Digit_with_small_values(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(1, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(1, 10, 3), 1)
        self.assertEqual(find_Nth_Digit(1, 10, 4), 0)
        self.assertEqual(find_Nth_Digit(1, 10, 5), 1)

    def test_find_Nth_Digit_with_large_values(self):
        self.assertEqual(find_Nth_Digit(100, 9, 1), 0)
        self.assertEqual(find_Nth_Digit(100, 9, 2), 9)
        self.assertEqual(find_Nth_Digit(100, 9, 3), 0)
        self.assertEqual(find_Nth_Digit(100, 9, 4), 9)
        self.assertEqual(find_Nth_Digit(100, 9, 5), 0)

    def test_find_Nth_Digit_with_large_N(self):
        self.assertEqual(find_Nth_Digit(100, 9, 10), 1)
        self.assertEqual(find_Nth_Digit(100, 9, 20), 0)
        self.assertEqual(find_Nth_Digit(100, 9, 30), 9)
        self.assertEqual(find_Nth_Digit(100, 9, 40), 0)
        self.assertEqual(find_Nth_Digit(100, 9, 50), 1)

import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_find_Nth_Digit(self):
        self.assertEqual(find_Nth_Digit(10, 3, 1), 3)
        self.assertEqual(find_Nth_Digit(10, 3, 2), 1)
        self.assertEqual(find_Nth_Digit(10, 3, 3), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 4), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 5), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 6), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 7), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 8), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 9), 0)
        self.assertEqual(find_Nth_Digit(10, 3, 10), 0)

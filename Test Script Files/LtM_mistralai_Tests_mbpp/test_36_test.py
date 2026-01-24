import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(10, 10, 2), 2)
        self.assertEqual(find_Nth_Digit(100, 10, 3), 3)
        self.assertEqual(find_Nth_Digit(1000, 10, 4), 4)

    def test_edge_cases(self):
        self.assertEqual(find_Nth_Digit(1, 10, 0), 0)
        self.assertEqual(find_Nth_Digit(10, 10, 0), 0)
        self.assertEqual(find_Nth_Digit(10, 10, 10), 9)
        self.assertEqual(find_Nth_Digit(1000000000, 10, 10), 0)

    def test_complex(self):
        self.assertEqual(find_Nth_Digit(1234567890, 10, 9), 9)
        self.assertEqual(find_Nth_Digit(1234567890, 10, 10), 0)
        self.assertEqual(find_Nth_Digit(1234567890, 10, 11), 1)

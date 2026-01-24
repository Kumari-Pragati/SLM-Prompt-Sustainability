import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(1, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(1, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(10, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(10, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(10, 10, 3), 9)
        self.assertEqual(find_Nth_Digit(100, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(100, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(100, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(1000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(1000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(1000, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(10000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(10000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(10000, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(100000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(100000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(100000, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(1000000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(1000000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(1000000, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(10000000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(10000000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(10000000, 10, 3), 7)
        self.assertEqual(find_Nth_Digit(100000000, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(100000000, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(100000000, 10, 3), 7)

    def test_edge_cases(self):
        self.assertEqual(find_Nth_Digit(1, 10, 0), 0)
        self.assertEqual(find_Nth_Digit(1, 10, -1), 0)
        self.assertEqual(find_Nth_Digit(1, 10, 4), 7)
        self.assertEqual(find_Nth_Digit(10, 10, 0), 0)
        self.assertEqual(find_Nth_Digit(10, 10, -1), 0)
        self.assertEqual(find_Nth_Digit(10, 10,
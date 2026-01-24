import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(10, 10, 2), 0)
        self.assertEqual(find_Nth_Digit(100, 10, 3), 0)
        self.assertEqual(find_Nth_Digit(1000, 10, 4), 1)
        self.assertEqual(find_Nth_Digit(10000, 10, 5), 0)
        self.assertEqual(find_Nth_Digit(100000, 10, 6), 1)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_Nth_Digit(1, 10, 0), None)
        self.assertEqual(find_Nth_Digit(1, 10, 10), None)
        self.assertEqual(find_Nth_Digit(10, 1, 1), None)
        self.assertEqual(find_Nth_Digit(10, 10, 0), None)
        self.assertEqual(find_Nth_Digit(10, 10, 11), None)
        self.assertEqual(find_Nth_Digit(0, 10, 1), None)
        self.assertEqual(find_Nth_Digit(10, 0, 1), None)

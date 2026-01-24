import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Nth_Digit(1, 9, 1), 1)
        self.assertEqual(find_Nth_Digit(10, 9, 2), 2)
        self.assertEqual(find_Nth_Digit(100, 9, 3), 3)
        self.assertEqual(find_Nth_Digit(1000, 9, 4), 4)
        self.assertEqual(find_Nth_Digit(10000, 9, 5), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Nth_Digit(1, 9, 0), 0)
        self.assertEqual(find_Nth_Digit(1, 9, 10), 9)
        self.assertEqual(find_Nth_Digit(9, 9, 1), 9)
        self.assertEqual(find_Nth_Digit(99, 9, 1), 1)
        self.assertEqual(find_Nth_Digit(999, 9, 1), 1)
        self.assertEqual(find_Nth_Digit(9999, 9, 1), 1)
        self.assertEqual(find_Nth_Digit(10000, 9, 2), 0)
        self.assertEqual(find_Nth_Digit(10000, 9, 3), 0)
        self.assertEqual(find_Nth_Digit(10000, 9, 4), 4)
        self.assertEqual(find_Nth_Digit(10000, 9, 5), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, find_Nth_Digit, 0, 9, 1)
        self.assertRaises(ValueError, find_Nth_Digit, 1, 0, 1)
        self.assertRaises(ValueError, find_Nth_Digit, 1, 9, 0)
        self.assertRaises(ValueError, find_Nth_Digit, 1, 9, -1)
        self.assertRaises(ValueError, find_Nth_Digit, 1000000000000, 9, 1)

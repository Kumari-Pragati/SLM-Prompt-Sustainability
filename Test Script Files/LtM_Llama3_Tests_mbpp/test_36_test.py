import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Nth_Digit(123, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(123, 10, 2), 2)
        self.assertEqual(find_Nth_Digit(123, 10, 3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_Nth_Digit(0, 10, 1), 0)
        self.assertEqual(find_Nth_Digit(123, 10, 0), None)
        self.assertEqual(find_Nth_Digit(123, 0, 1), None)

    def test_complex_inputs(self):
        self.assertEqual(find_Nth_Digit(123456, 10, 5), 6)
        self.assertEqual(find_Nth_Digit(123456, 100, 2), 4)
        self.assertEqual(find_Nth_Digit(123456, 1000, 3), 5)

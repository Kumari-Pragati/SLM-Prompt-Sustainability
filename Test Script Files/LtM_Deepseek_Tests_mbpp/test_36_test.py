import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Nth_Digit(1, 2, 3), 1)
        self.assertEqual(find_Nth_Digit(10, 2, 3), 1)
        self.assertEqual(find_Nth_Digit(100, 2, 3), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find_Nth_Digit(0, 1, 1), 0)
        self.assertEqual(find_Nth_Digit(1, 1, 1), 1)
        self.assertEqual(find_Nth_Digit(1, 1, 0), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_Nth_Digit(1, 0, 1), 0)
        self.assertEqual(find_Nth_Digit(1, 0, 0), 1)
        self.assertEqual(find_Nth_Digit(1, 2, -1), 1)

    def test_complex_cases(self):
        self.assertEqual(find_Nth_Digit(123, 100, 2), 2)
        self.assertEqual(find_Nth_Digit(123, 100, 3), 3)
        self.assertEqual(find_Nth_Digit(123, 100, 4), 1)

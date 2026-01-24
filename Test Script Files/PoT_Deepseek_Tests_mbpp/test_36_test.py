import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Nth_Digit(1, 2, 3), 1)
        self.assertEqual(find_Nth_Digit(10, 3, 2), 1)
        self.assertEqual(find_Nth_Digit(100, 10, 3), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Nth_Digit(0, 1, 1), 0)
        self.assertEqual(find_Nth_Digit(1, 0, 1), 1)
        self.assertEqual(find_Nth_Digit(1, 1, 0), 1)
        self.assertEqual(find_Nth_Digit(1, 1, 1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(1, 0, 1)
        with self.assertRaises(TypeError):
            find_Nth_Digit("1", 1, 1)
        with self.assertRaises(TypeError):
            find_Nth_Digit(1, "1", 1)
        with self.assertRaises(TypeError):
            find_Nth_Digit(1, 1, "1")

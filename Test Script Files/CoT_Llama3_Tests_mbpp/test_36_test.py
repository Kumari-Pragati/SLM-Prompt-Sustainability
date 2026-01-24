import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Nth_Digit(123, 456, 1), 3)
        self.assertEqual(find_Nth_Digit(123, 456, 2), 2)
        self.assertEqual(find_Nth_Digit(123, 456, 3), 1)
        self.assertEqual(find_Nth_Digit(123, 456, 4), 4)

    def test_edge_cases(self):
        self.assertEqual(find_Nth_Digit(0, 0, 1), 0)
        self.assertEqual(find_Nth_Digit(0, 0, 2), 0)
        self.assertEqual(find_Nth_Digit(0, 0, 3), 0)
        self.assertEqual(find_Nth_Digit(0, 0, 4), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Nth_Digit('123', 456, 1)
        with self.assertRaises(TypeError):
            find_Nth_Digit(123, '456', 1)
        with self.assertRaises(TypeError):
            find_Nth_Digit(123, 456, '1')

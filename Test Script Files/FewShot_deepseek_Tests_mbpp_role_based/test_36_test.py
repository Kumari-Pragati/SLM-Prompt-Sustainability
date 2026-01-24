import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Nth_Digit(10, 3, 2), 3)

    def test_boundary_conditions(self):
        self.assertEqual(find_Nth_Digit(1, 1, 1), 1)
        self.assertEqual(find_Nth_Digit(10, 1, 1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Nth_Digit('10', 3, 2)
        with self.assertRaises(TypeError):
            find_Nth_Digit(10, '3', 2)
        with self.assertRaises(TypeError):
            find_Nth_Digit(10, 3, '2')
        with self.assertRaises(ValueError):
            find_Nth_Digit(10, 0, 1)
        with self.assertRaises(ValueError):
            find_Nth_Digit(10, 3, -1)

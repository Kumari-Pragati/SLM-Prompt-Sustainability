import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_different_numbers_with_difference_less_than_5(self):
        self.assertEqual(compute_Last_Digit(3, 6), 3)
        self.assertEqual(compute_Last_Digit(6, 3), 3)

    def test_different_numbers_with_difference_greater_or_equal_to_5(self):
        self.assertEqual(compute_Last_Digit(3, 8), 0)
        self.assertEqual(compute_Last_Digit(8, 3), 0)

    def test_zero(self):
        self.assertEqual(compute_Last_Digit(0, 5), 0)
        self.assertEqual(compute_Last_Digit(5, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(compute_Last_Digit(-3, -5), 3)
        self.assertEqual(compute_Last_Digit(-5, -3), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, compute_Last_Digit, 'a', 'b')
        self.assertRaises(TypeError, compute_Last_Digit, 1.5, 2)

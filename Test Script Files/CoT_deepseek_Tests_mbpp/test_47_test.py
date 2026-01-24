import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_difference_greater_than_five(self):
        self.assertEqual(compute_Last_Digit(1, 7), 0)
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_typical_cases(self):
        self.assertEqual(compute_Last_Digit(1, 5), 120)
        self.assertEqual(compute_Last_Digit(2, 6), 48)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit("1", 2)
        with self.assertRaises(TypeError):
            compute_Last_Digit(1, "2")
        with self.assertRaises(TypeError):
            compute_Last_Digit("1", "2")
        with self.assertRaises(ValueError):
            compute_Last_Digit(10, 9)

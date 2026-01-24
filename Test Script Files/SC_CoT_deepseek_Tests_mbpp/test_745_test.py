import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 12, 14, 15, 18, 20])

    def test_single_digit_numbers(self):
        self.assertEqual(divisible_by_digits(1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_boundary_conditions(self):
        self.assertEqual(divisible_by_digits(0, 0), [0])
        self.assertEqual(divisible_by_digits(1, 1), [])

    def test_edge_cases(self):
        self.assertEqual(divisible_by_digits(10, 2), [10, 12])
        self.assertEqual(divisible_by_digits(100, 101), [100, 102])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            divisible_by_digits("10", 20)
        with self.assertRaises(TypeError):
            divisible_by_digits(10, "20")
        with self.assertRaises(TypeError):
            divisible_by_digits("10", "20")
        with self.assertRaises(ValueError):
            divisible_by_digits(-10, 20)
        with self.assertRaises(ValueError):
            divisible_by_digits(10, -20)

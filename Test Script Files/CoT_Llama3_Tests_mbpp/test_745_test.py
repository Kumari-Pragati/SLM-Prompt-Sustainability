import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 5, 7, 9])

    def test_edge_case_start_zero(self):
        self.assertEqual(divisible_by_digits(0, 10), [1, 2, 3, 5, 7, 9])

    def test_edge_case_end_zero(self):
        self.assertEqual(divisible_by_digits(1, 0), [])

    def test_edge_case_start_end_equal(self):
        self.assertEqual(divisible_by_digits(5, 5), [5])

    def test_edge_case_start_end_zero(self):
        self.assertEqual(divisible_by_digits(0, 0), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('a', 10)

    def test_invalid_input_range(self):
        with self.assertRaises(ValueError):
            divisible_by_digits(10, 5)

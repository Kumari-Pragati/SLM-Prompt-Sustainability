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

    def test_edge_case_start_end_equal_with_zero(self):
        self.assertEqual(divisible_by_digits(0, 0), [])

    def test_edge_case_start_greater_than_end(self):
        self.assertEqual(divisible_by_digits(10, 5), [])

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('a', 10)

    def test_edge_case_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            divisible_by_digits(1, 'a')

    def test_edge_case_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('a', 'b')

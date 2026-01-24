import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(divisible_by_digits(12, 20), [12, 13, 14, 15, 16, 17, 18, 19])

    def test_edge_case_start_num(self):
        self.assertListEqual(divisible_by_digits(0, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_end_num(self):
        self.assertListEqual(divisible_by_digits(100, 100), [100])

    def test_boundary_case_start_end_num(self):
        self.assertListEqual(divisible_by_digits(1, 1), [1])

    def test_invalid_input_start_num(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('a', 10)

    def test_invalid_input_end_num(self):
        with self.assertRaises(TypeError):
            divisible_by_digits(10, 'a')

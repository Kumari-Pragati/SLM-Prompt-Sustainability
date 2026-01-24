import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 12, 14, 15, 18, 20])

    def test_edge_boundary_conditions(self):
        self.assertEqual(divisible_by_digits(1, 1), [1])
        self.assertEqual(divisible_by_digits(100, 100), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            divisible_by_digits('10', 20)
        with self.assertRaises(TypeError):
            divisible_by_digits(10, '20')
        with self.assertRaises(TypeError):
            divisible_by_digits('10', '20')
        with self.assertRaises(ValueError):
            divisible_by_digits(20, 10)

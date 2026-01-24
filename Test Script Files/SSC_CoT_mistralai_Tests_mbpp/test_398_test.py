import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 21)
        self.assertEqual(sum_of_digits([0]), 0)
        self.assertEqual(sum_of_digits([10, 20, 30]), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_of_digits([0.5, -1]), 0)
        self.assertEqual(sum_of_digits([1000]), 1)
        self.assertEqual(sum_of_digits([1234567890]), 63)
        self.assertEqual(sum_of_digits([12345678901]), 91)

    def test_special_cases(self):
        self.assertEqual(sum_of_digits([12.345, 'abc']), 0)
        self.assertEqual(sum_of_digits([True, False]), 0)
        self.assertEqual(sum_of_digits([None]), 0)

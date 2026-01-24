import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 6)

    def test_edge_case_single_digit(self):
        self.assertEqual(sum_of_digits([1]), 1)

    def test_edge_case_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(sum_of_digits([-1, 2, 3]), 4)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_edge_case_non_integer_input(self):
        self.assertEqual(sum_of_digits([1, '2', 3]), 6)

    def test_edge_case_mixed_types(self):
        self.assertEqual(sum_of_digits([1, 2, 3.5]), 6)

    def test_edge_case_large_input(self):
        self.assertEqual(sum_of_digits([i for i in range(100)]), 4500)

    def test_edge_case_large_negative_input(self):
        self.assertEqual(sum_of_digits([-i for i in range(100)]), -4500)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(sum_of_digits([-1, 2, -3, 4]), 3)

    def test_edge_case_mixed_types_and_signs(self):
        self.assertEqual(sum_of_digits([-1, '2', -3, 4]), 5)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            sum_of_digits("Invalid input")

    def test_invalid_input_non_iterable_list(self):
        with self.assertRaises(TypeError):
            sum_of_digits([1, "Invalid input"])

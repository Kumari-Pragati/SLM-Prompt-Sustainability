import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_multiple_digits(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_zero(self):
        self.assertEqual(multiple_to_single([0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            multiple_to_single([])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            multiple_to_single([1, '2', 3])

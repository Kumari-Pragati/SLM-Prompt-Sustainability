import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(multiple_to_single([]), None)

    def test_single_digit(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_multiple_digits(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_mixed_signs(self):
        self.assertEqual(multiple_to_single([1, -2, 3]), 13)

    def test_large_numbers(self):
        self.assertEqual(multiple_to_single([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), 9999999999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiple_to_single("abc")

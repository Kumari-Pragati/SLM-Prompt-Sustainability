import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_single_digit_input(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_multiple_digit_input(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_input_with_zero(self):
        self.assertEqual(multiple_to_single([0, 1, 2]), 12)

    def test_input_with_zero_at_start(self):
        self.assertEqual(multiple_to_single([0, 2, 3]), 23)

    def test_input_with_zero_at_end(self):
        self.assertEqual(multiple_to_single([1, 2, 0]), 120)

    def test_input_with_zero_in_middle(self):
        self.assertEqual(multiple_to_single([1, 0, 2]), 12)

    def test_input_with_non_digit_characters(self):
        with self.assertRaises(ValueError):
            multiple_to_single(['a', 'b', 'c'])

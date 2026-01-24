import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_two_digits(self):
        self.assertEqual(multiple_to_single([1, 2]), 12)

    def test_three_digits(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_multiple_digits(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            multiple_to_single([])

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            multiple_to_single(['a', 'b', 'c'])

    def test_mixed_type_input(self):
        with self.assertRaises(ValueError):
            multiple_to_single([1, 'a', 3])

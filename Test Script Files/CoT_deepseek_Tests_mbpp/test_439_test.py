import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4]), 1234)

    def test_single_digit(self):
        self.assertEqual(multiple_to_single([5]), 5)

    def test_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3, -4]), -1234)

    def test_mixed_numbers(self):
        self.assertEqual(multiple_to_single([0, 1, 2, 3]), 1230)

    def test_large_numbers(self):
        self.assertEqual(multiple_to_single([9, 9, 9, 9]), 9999)

    def test_decimal_numbers(self):
        with self.assertRaises(TypeError):
            multiple_to_single([1.1, 2.2, 3.3, 4.4])

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            multiple_to_single(["1", "2", "3", "4"])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            multiple_to_single([1, "2", 3, "4"])

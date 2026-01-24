import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(convert([1, 2, 3, 4]), 1234)

    def test_single_digit_case(self):
        self.assertEqual(convert([5]), 5)

    def test_empty_list_case(self):
        self.assertEqual(convert([]), 0)

    def test_negative_numbers_case(self):
        self.assertEqual(convert([-1, -2, -3, -4]), -1234)

    def test_zero_in_list_case(self):
        self.assertEqual(convert([0, 1, 2, 3]), 1230)

    def test_large_numbers_case(self):
        self.assertEqual(convert([9, 9, 9, 9, 9]), 99999)

    def test_mixed_positive_negative_case(self):
        self.assertEqual(convert([-1, 2, -3, 4]), -1234)

    def test_float_numbers_case(self):
        with self.assertRaises(TypeError):
            convert([1.1, 2.2, 3.3])

    def test_string_numbers_case(self):
        with self.assertRaises(TypeError):
            convert(["1", "2", "3"])

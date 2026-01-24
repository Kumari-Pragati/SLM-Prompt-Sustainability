import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(convert([1, 2, 3, 4]), 1234)

    def test_single_digit(self):
        self.assertEqual(convert([5]), 5)

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3, -4]), -1234)

    def test_mixed_numbers(self):
        self.assertEqual(convert([0, 9, 8, 7, 6]), 98760)

    def test_large_numbers(self):
        self.assertEqual(convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 1234567890)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            convert([1, 2, '3', 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            convert(1234)

import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_list_of_integers(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_convert_list_of_negative_integers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_convert_list_of_mixed_integers(self):
        self.assertEqual(convert([1, -2, 3]), 13)

    def test_convert_list_of_zero(self):
        self.assertEqual(convert([0]), 0)

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_convert_list_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            convert([1, 'a', 3])

    def test_convert_list_with_non_integer_values_and_negative(self):
        with self.assertRaises(TypeError):
            convert([-1, 'a', 3])

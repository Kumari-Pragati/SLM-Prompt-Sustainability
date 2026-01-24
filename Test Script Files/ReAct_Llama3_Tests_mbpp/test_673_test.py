import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_convert_single_element_list(self):
        self.assertEqual(convert([1]), 1)

    def test_convert_multiple_elements_list(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_convert_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_convert_mixed_positive_and_negative_numbers(self):
        self.assertEqual(convert([1, -2, 3]), 13)

    def test_convert_list_with_zero(self):
        self.assertEqual(convert([0, 1, 2]), 102)

    def test_convert_list_with_duplicates(self):
        self.assertEqual(convert([1, 1, 2, 2, 3]), 111223)

    def test_convert_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            convert([1, 'a', 3])

    def test_convert_list_with_non_list_input(self):
        with self.assertRaises(TypeError):
            convert('abc')

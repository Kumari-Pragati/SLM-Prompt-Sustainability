import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_single_element_list(self):
        self.assertEqual(convert([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), 321)

    def test_mixed_numbers(self):
        self.assertEqual(convert([1, -2, 3, -4, 5]), 135)

    def test_zero(self):
        self.assertEqual(convert([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(convert([1000000001, 1000000002, 1000000003]), 3000000006)

    def test_string_input(self):
        self.assertRaises(ValueError, convert, ['a', 'b', 'c'])

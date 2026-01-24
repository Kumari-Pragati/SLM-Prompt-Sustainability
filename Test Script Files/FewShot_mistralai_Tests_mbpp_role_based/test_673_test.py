import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(convert([1, 2, 3, 4]), 1234)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3, -4]), 1234)

    def test_zero(self):
        self.assertEqual(convert([0]), 0)

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            convert([1, "2", 3])

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            convert([1.1, 2.2, 3.3])

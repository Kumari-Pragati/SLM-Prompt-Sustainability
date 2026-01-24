import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(convert([0, 1, 2, 3, 4, 5]), 012345)
        self.assertEqual(convert([9, 8, 7, 6, 5]), 98765)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3, -4, -5]), 12345)
        self.assertEqual(convert([0, -1, -2, -3, -4, -5]), -012345)
        self.assertEqual(convert([-9, -8, -7, -6, -5]), -98765)

    def test_mixed_numbers(self):
        self.assertEqual(convert([1, -2, 3, -4, 5]), 135-4)
        self.assertEqual(convert([0, 1, -2, 3, -4, 5]), 013-45)
        self.assertEqual(convert([-9, 8, -7, 6, -5]), -986-5)

    def test_single_number(self):
        self.assertEqual(convert([1]), 1)
        self.assertEqual(convert([-1]), -1)
        self.assertEqual(convert([0]), 0)

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, convert, [1, "a", 2])
        self.assertRaises(TypeError, convert, ["1", "a", "2"])

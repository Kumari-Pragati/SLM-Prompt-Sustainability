import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(find_rect_num(3), 6)
        self.assertEqual(find_rect_num(5), 15)
        self.assertEqual(find_rect_num(10), 55)

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_integer(self):
        self.assertEqual(find_rect_num(-1), 0)
        self.assertEqual(find_rect_num(-2), 2)
        self.assertEqual(find_rect_num(-10), 0)

    def test_floats(self):
        self.assertEqual(find_rect_num(2.5), 7.5)
        self.assertEqual(find_rect_num(-3.2), 0)

    def test_strings(self):
        with self.assertRaises(ValueError):
            find_rect_num('abc')

    def test_lists(self):
        with self.assertRaises(TypeError):
            find_rect_num([1, 2, 3])

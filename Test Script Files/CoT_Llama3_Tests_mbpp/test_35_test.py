import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_rect_num(1), 1)
        self.assertEqual(find_rect_num(2), 3)
        self.assertEqual(find_rect_num(3), 6)
        self.assertEqual(find_rect_num(4), 10)
        self.assertEqual(find_rect_num(5), 15)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            find_rect_num(-1)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            find_rect_num(1.5)

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_large_numbers(self):
        self.assertEqual(find_rect_num(100), 10100)

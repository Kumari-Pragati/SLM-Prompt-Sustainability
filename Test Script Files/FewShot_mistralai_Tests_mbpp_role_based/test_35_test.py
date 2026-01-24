import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(find_rect_num(5), 21)

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_integer(self):
        self.assertEqual(find_rect_num(-3), 12)

    def test_large_integer(self):
        self.assertEqual(find_rect_num(100), 5050)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_rect_num(3.14)

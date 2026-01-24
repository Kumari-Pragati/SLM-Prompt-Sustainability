import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_rect_num(3), 6)

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_rect_num(-3), -6)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_rect_num(3.5)

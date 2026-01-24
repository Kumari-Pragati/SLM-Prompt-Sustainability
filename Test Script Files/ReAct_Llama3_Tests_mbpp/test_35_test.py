import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_positive(self):
        self.assertEqual(find_rect_num(5), 30)

    def test_negative(self):
        with self.assertRaises(TypeError):
            find_rect_num(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_rect_num(3.5)

    def test_large_number(self):
        self.assertEqual(find_rect_num(1000), 1001000)

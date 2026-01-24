import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)
        self.assertEqual(find_rect_num(10), 110)

    def test_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            find_rect_num(-1)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            find_rect_num(1.5)
        with self.assertRaises(TypeError):
            find_rect_num('1')

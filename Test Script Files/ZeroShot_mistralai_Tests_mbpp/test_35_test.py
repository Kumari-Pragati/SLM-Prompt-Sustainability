import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_find_rect_num_positive(self):
        self.assertEqual(find_rect_num(1), 1)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(5), 5 * 6)

    def test_find_rect_num_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_find_rect_num_negative(self):
        self.assertEqual(find_rect_num(-1), -1)
        self.assertEqual(find_rect_num(-2), 5)

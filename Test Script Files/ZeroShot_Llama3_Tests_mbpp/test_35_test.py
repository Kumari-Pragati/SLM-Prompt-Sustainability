import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_find_rect_num(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1), 1)
        self.assertEqual(find_rect_num(2), 3)
        self.assertEqual(find_rect_num(3), 6)
        self.assertEqual(find_rect_num(4), 10)
        self.assertEqual(find_rect_num(5), 15)
        self.assertEqual(find_rect_num(6), 21)
        self.assertEqual(find_rect_num(7), 28)
        self.assertEqual(find_rect_num(8), 36)
        self.assertEqual(find_rect_num(9), 45)
        self.assertEqual(find_rect_num(10), 55)

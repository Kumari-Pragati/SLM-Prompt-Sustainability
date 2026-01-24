import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_find_rect_num(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)
        self.assertEqual(find_rect_num(4), 20)
        self.assertEqual(find_rect_num(5), 30)
        self.assertEqual(find_rect_num(6), 42)
        self.assertEqual(find_rect_num(7), 56)
        self.assertEqual(find_rect_num(8), 72)
        self.assertEqual(find_rect_num(9), 90)
        self.assertEqual(find_rect_num(10), 110)

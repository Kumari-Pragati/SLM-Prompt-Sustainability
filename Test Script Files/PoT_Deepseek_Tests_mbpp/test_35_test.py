import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(5), 30)
        self.assertEqual(find_rect_num(10), 110)

    def test_edge_cases(self):
        self.assertEqual(find_rect_num(0), 1)

    def test_corner_cases(self):
        self.assertEqual(find_rect_num(-1), 0)
        self.assertEqual(find_rect_num(100), 10100)

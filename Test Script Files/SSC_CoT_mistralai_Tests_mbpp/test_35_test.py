import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_rect_num(5), 20)
        self.assertEqual(find_rect_num(10), 100)

    def test_edge_cases(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, find_rect_num, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, find_rect_num, 3.14)

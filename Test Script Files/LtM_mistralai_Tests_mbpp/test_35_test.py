import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_rect_num(1), 1)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1000), 1000001)
        self.assertEqual(find_rect_num(-1), -1)

import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_rect_num(5), 15)

    def test_edge_case_zero(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(find_rect_num(1), 1)

    def test_boundary_case_negative(self):
        self.assertEqual(find_rect_num(-1), None)

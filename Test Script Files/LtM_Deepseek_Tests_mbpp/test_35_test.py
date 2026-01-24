import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)

    def test_edge_conditions(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(-1), 0)

    def test_complex_cases(self):
        self.assertEqual(find_rect_num(10), 110)
        self.assertEqual(find_rect_num(20), 210)

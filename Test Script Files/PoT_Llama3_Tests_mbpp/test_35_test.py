import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_rect_num(5), 30)

    def test_edge_case(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_edge_case2(self):
        self.assertEqual(find_rect_num(-1), -1)

    def test_edge_case3(self):
        self.assertEqual(find_rect_num(1), 2)

    def test_edge_case4(self):
        self.assertEqual(find_rect_num(2), 3)

    def test_edge_case5(self):
        self.assertEqual(find_rect_num(3), 6)

    def test_edge_case6(self):
        self.assertEqual(find_rect_num(4), 10)

    def test_edge_case7(self):
        self.assertEqual(find_rect_num(5), 15)

    def test_edge_case8(self):
        self.assertEqual(find_rect_num(6), 21)

    def test_edge_case9(self):
        self.assertEqual(find_rect_num(7), 28)

    def test_edge_case10(self):
        self.assertEqual(find_rect_num(8), 36)

    def test_edge_case11(self):
        self.assertEqual(find_rect_num(9), 45)

    def test_edge_case12(self):
        self.assertEqual(find_rect_num(10), 55)

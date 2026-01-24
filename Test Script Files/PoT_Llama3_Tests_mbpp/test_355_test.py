import unittest
from mbpp_355_code import count_Rectangles

class TestCount_Rectangles(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rectangles(1), 1)

    def test_edge_case(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_edge_case2(self):
        self.assertEqual(count_Rectangles(2), 4)

    def test_edge_case3(self):
        self.assertEqual(count_Rectangles(3), 9)

    def test_edge_case4(self):
        self.assertEqual(count_Rectangles(4), 16)

    def test_edge_case5(self):
        self.assertEqual(count_Rectangles(5), 25)

    def test_edge_case6(self):
        self.assertEqual(count_Rectangles(6), 36)

    def test_edge_case7(self):
        self.assertEqual(count_Rectangles(7), 49)

    def test_edge_case8(self):
        self.assertEqual(count_Rectangles(8), 64)

    def test_edge_case9(self):
        self.assertEqual(count_Rectangles(9), 81)

    def test_edge_case10(self):
        self.assertEqual(count_Rectangles(10), 100)

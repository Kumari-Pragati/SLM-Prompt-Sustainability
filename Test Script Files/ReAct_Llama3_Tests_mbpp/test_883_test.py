import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_div_of_nums_typical(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 2, 3), [3, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 72, 78, 84, 90, 96, 100])

    def test_div_of_nums_edge_case1(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100])

    def test_div_of_nums_edge_case2(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 0, 1), [])

    def test_div_of_nums_edge_case3(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 1, 0), [])

    def test_div_of_nums_edge_case4(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 0, 0), [])

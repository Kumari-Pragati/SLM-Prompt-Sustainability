import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_div_of_nums_typical(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 3), [2, 3, 4, 6, 8, 9])

    def test_div_of_nums_edge_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_div_of_nums_edge_case2(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_div_of_nums_edge_case3(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 5), [5])

    def test_div_of_nums_edge_case4(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 3), [3])

    def test_div_of_nums_edge_case5(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 2), [2, 4, 6, 8, 10])

    def test_div_of_nums_edge_case6(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 1), [])

    def test_div_of_nums_edge_case7(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10), [])

    def test_div_of_nums_edge_case8(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 10), [5])

    def test_div_of_nums_edge_case9(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 5), [5])

    def test_div_of_nums_edge_case10(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 10), [2, 4, 6, 8, 10])

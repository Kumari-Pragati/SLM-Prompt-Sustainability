import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_get_max_sum_typical(self):
        self.assertEqual(get_max_sum(10), 34)

    def test_get_max_sum_edge_case(self):
        self.assertEqual(get_max_sum(5), 5)

    def test_get_max_sum_edge_case2(self):
        self.assertEqual(get_max_sum(1), 1)

    def test_get_max_sum_edge_case3(self):
        self.assertEqual(get_max_sum(2), 2)

    def test_get_max_sum_edge_case4(self):
        self.assertEqual(get_max_sum(3), 3)

    def test_get_max_sum_edge_case5(self):
        self.assertEqual(get_max_sum(4), 4)

    def test_get_max_sum_edge_case6(self):
        self.assertEqual(get_max_sum(6), 6)

    def test_get_max_sum_edge_case7(self):
        self.assertEqual(get_max_sum(7), 7)

    def test_get_max_sum_edge_case8(self):
        self.assertEqual(get_max_sum(8), 8)

    def test_get_max_sum_edge_case9(self):
        self.assertEqual(get_max_sum(9), 9)

    def test_get_max_sum_edge_case10(self):
        self.assertEqual(get_max_sum(10), 10)

    def test_get_max_sum_edge_case11(self):
        self.assertEqual(get_max_sum(11), 11)

    def test_get_max_sum_edge_case12(self):
        self.assertEqual(get_max_sum(12), 12)

    def test_get_max_sum_edge_case13(self):
        self.assertEqual(get_max_sum(13), 13)

    def test_get_max_sum_edge_case14(self):
        self.assertEqual(get_max_sum(14), 14)

    def test_get_max_sum_edge_case15(self):
        self.assertEqual(get_max_sum(15), 15)

    def test_get_max_sum_edge_case16(self):
        self.assertEqual(get_max_sum(16), 16)

    def test_get_max_sum_edge_case17(self):
        self.assertEqual(get_max_sum(17), 17)

    def test_get_max_sum_edge_case18(self):
        self.assertEqual(get_max_sum(18), 18)

    def test_get_max_sum_edge_case19(self):
        self.assertEqual(get_max_sum(19), 19)

    def test_get_max_sum_edge_case20(self):
        self.assertEqual(get_max_sum(20), 20)

import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_difference(10), 264)

    def test_edge_case(self):
        self.assertEqual(sum_difference(1), 0)

    def test_edge_case2(self):
        self.assertEqual(sum_difference(2), 4)

    def test_edge_case3(self):
        self.assertEqual(sum_difference(3), 0)

    def test_edge_case4(self):
        self.assertEqual(sum_difference(4), 30)

    def test_edge_case5(self):
        self.assertEqual(sum_difference(5), 0)

    def test_edge_case6(self):
        self.assertEqual(sum_difference(6), 36)

    def test_edge_case7(self):
        self.assertEqual(sum_difference(7), 0)

    def test_edge_case8(self):
        self.assertEqual(sum_difference(8), 64)

    def test_edge_case9(self):
        self.assertEqual(sum_difference(9), 0)

    def test_edge_case10(self):
        self.assertEqual(sum_difference(10), 264)

    def test_edge_case11(self):
        self.assertEqual(sum_difference(11), 0)

    def test_edge_case12(self):
        self.assertEqual(sum_difference(12), 300)

    def test_edge_case13(self):
        self.assertEqual(sum_difference(13), 0)

    def test_edge_case14(self):
        self.assertEqual(sum_difference(14), 336)

    def test_edge_case15(self):
        self.assertEqual(sum_difference(15), 0)

    def test_edge_case16(self):
        self.assertEqual(sum_difference(16), 374)

    def test_edge_case17(self):
        self.assertEqual(sum_difference(17), 0)

    def test_edge_case18(self):
        self.assertEqual(sum_difference(18), 414)

    def test_edge_case19(self):
        self.assertEqual(sum_difference(19), 0)

    def test_edge_case20(self):
        self.assertEqual(sum_difference(20), 456)

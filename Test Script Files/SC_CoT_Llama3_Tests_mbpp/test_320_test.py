import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_difference(10), 264)

    def test_edge_case(self):
        self.assertEqual(sum_difference(1), 0)

    def test_edge_case2(self):
        self.assertEqual(sum_difference(0), 0)

    def test_edge_case3(self):
        self.assertEqual(sum_difference(-1), None)

    def test_edge_case4(self):
        with self.assertRaises(TypeError):
            sum_difference("a")

    def test_edge_case5(self):
        with self.assertRaises(TypeError):
            sum_difference([1, 2, 3])

    def test_edge_case6(self):
        with self.assertRaises(TypeError):
            sum_difference(None)

    def test_edge_case7(self):
        with self.assertRaises(TypeError):
            sum_difference({"a": 1})

import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 4), 10)

    def test_edge_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 3, 5], 5, 0, 4), 9)

    def test_edge_case2(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 1, 4), 9)

    def test_edge_case3(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 0), 2)

    def test_edge_case4(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 1, 0), 1)

    def test_edge_case5(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 4), 5)

    def test_edge_case6(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 3), 7)

    def test_edge_case7(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 1, 3), 7)

    def test_edge_case8(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 2, 4), 8)

    def test_edge_case9(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 3, 4), 9)

    def test_edge_case10(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 0), 1)

    def test_edge_case11(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 1), 2)

    def test_edge_case12(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 2), 3)

    def test_edge_case13(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 3), 4)

    def test_edge_case14(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 4), 5)

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq("a", 5, 0, 4)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], "a", 0, 4)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, "a", 4)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, "a")

    def test_invalid_input5(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, -1)

    def test_invalid_input6(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 5)

    def test_invalid_input7(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, -1, 4)

    def test_invalid_input8(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subseq([1, 2, 3, 4, 5],
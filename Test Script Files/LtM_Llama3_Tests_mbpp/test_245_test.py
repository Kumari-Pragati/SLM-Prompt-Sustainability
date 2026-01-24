import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge1(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 1), 1)

    def test_edge2(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 0), float("-Inf"))

    def test_edge3(self):
        self.assertEqual(max_sum([], 0), float("-Inf"))

    def test_edge4(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge5(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 6), float("-Inf"))

    def test_edge6(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], -1), float("-Inf"))

    def test_edge7(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge8(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge9(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge10(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge11(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge12(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge13(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge14(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge15(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge16(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge17(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge18(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge19(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge20(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

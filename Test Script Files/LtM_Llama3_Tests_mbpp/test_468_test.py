import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 20)

    def test_edge_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 0], 5), 4)

    def test_edge_case2(self):
        self.assertEqual(max_product([1, 2, 3, 0, 0], 5), 0)

    def test_edge_case3(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case4(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case5(self):
        self.assertEqual(max_product([], 0), 0)

    def test_edge_case6(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 6), 20)

    def test_edge_case7(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6], 6), 20)

    def test_edge_case8(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7], 7), 35)

    def test_edge_case9(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7, 8], 8), 40)

    def test_edge_case10(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 45)

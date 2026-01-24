import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case(self):
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case3(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 0), 1)

    def test_edge_case4(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 6), 1)

    def test_edge_case5(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case6(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 2), 2)

    def test_edge_case7(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case8(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 4), 24)

    def test_edge_case9(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case10(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 6), 1)

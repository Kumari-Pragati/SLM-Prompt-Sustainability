import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 0), 1)

    def test_edge_case3(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 6), 1)

    def test_edge_case4(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], -1), 1)

    def test_edge_case5(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 7), 1)

    def test_edge_case6(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 8), 1)

    def test_edge_case7(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 9), 1)

    def test_edge_case8(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 10), 1)

    def test_edge_case9(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 11), 1)

    def test_edge_case10(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 12), 1)

    def test_edge_case11(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 13), 1)

    def test_edge_case12(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 14), 1)

    def test_edge_case13(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 15), 1)

    def test_edge_case14(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 16), 1)

    def test_edge_case15(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 17), 1)

    def test_edge_case16(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 18), 1)

    def test_edge_case17(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 19), 1)

    def test_edge_case18(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 20), 1)

    def test_edge_case19(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 21), 1)

    def test_edge_case20(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 22), 1)

    def test_edge_case21(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 23), 1)

    def test_edge_case22(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 24), 1)

    def test_edge_case23(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 25), 120)

    def test_edge_case24(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 26), 1)

    def test_edge_case25(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 27), 1)

    def test_edge_case26(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 28), 1)

    def test_edge_case27(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 29), 1)

    def test_edge_case28(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 30), 1)

    def test_edge_case29(self):
        self.assertEqual(find_Product([1, 2, 3
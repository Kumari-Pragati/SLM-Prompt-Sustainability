import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 1), 30)

    def test_edge_case(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 0), 1)

    def test_edge_case2(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 3), 6)

    def test_edge_case3(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 4), 6)

    def test_edge_case4(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 5), 6)

    def test_edge_case5(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 6), 6)

    def test_edge_case6(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 7), 1)

    def test_edge_case7(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 8), 1)

    def test_edge_case8(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 9), 1)

    def test_edge_case9(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 10), 1)

    def test_edge_case10(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 11), 1)

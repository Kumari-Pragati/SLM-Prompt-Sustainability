import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case(self):
        self.assertEqual(equilibrium_index([1, 1]), 0)

    def test_edge_case2(self):
        self.assertEqual(equilibrium_index([1, 2, 1]), 0)

    def test_edge_case3(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

    def test_edge_case4(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 5)

    def test_edge_case5(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), -1)

    def test_edge_case6(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), -1)

    def test_edge_case7(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), -1)

    def test_edge_case8(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), -1)

    def test_edge_case9(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), -1)

    def test_edge_case10(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), -1)

    def test_edge_case11(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), -1)

    def test_edge_case12(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), -1)

    def test_edge_case13(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), -1)

    def test_edge_case14(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), -1)

    def test_edge_case15(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), -1)

    def test_edge_case16(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), -1)

    def test_edge_case17(self):
        self.assertEqual(equ
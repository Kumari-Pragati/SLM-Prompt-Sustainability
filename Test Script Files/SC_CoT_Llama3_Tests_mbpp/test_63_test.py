import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_edge2(self):
        self.assertEqual(max_difference([(1, 3), (2, 4), (5, 6)]), 2)

    def test_edge3(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge4(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4)]), 1)

    def test_edge5(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)

    def test_edge6(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]), 1)

    def test_edge7(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]), 1)

    def test_edge8(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]), 1)

    def test_edge9(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]), 1)

    def test_edge10(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]), 1)

    def test_edge11(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]), 1)

    def test_edge12(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]), 1)

    def test_edge13(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13)]), 1)

    def test_edge14(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14)]), 1)

    def test_edge15(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)]), 1)

    def test_edge16(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (
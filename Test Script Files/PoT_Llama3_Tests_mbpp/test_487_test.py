import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_tuple((1, 3, 2)), (1, 2, 3))

    def test_edge_case(self):
        self.assertEqual(sort_tuple((1, 2)), (1, 2))

    def test_edge_case2(self):
        self.assertEqual(sort_tuple((2, 1)), (1, 2))

    def test_edge_case3(self):
        self.assertEqual(sort_tuple(()), ())

    def test_edge_case4(self):
        self.assertEqual(sort_tuple((1)), (1,))

    def test_edge_case5(self):
        self.assertEqual(sort_tuple((1, 2, 3, 4)), (1, 2, 3, 4))

    def test_edge_case6(self):
        self.assertEqual(sort_tuple((4, 3, 2, 1)), (1, 2, 3, 4))

    def test_edge_case7(self):
        self.assertEqual(sort_tuple((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case8(self):
        self.assertEqual(sort_tuple((5, 4, 3, 2, 1)), (1, 2, 3, 4, 5))

    def test_edge_case9(self):
        self.assertEqual(sort_tuple((1, 2, 3, 4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_edge_case10(self):
        self.assertEqual(sort_tuple((6, 5, 4, 3, 2, 1)), (1, 2, 3, 4, 5, 6))

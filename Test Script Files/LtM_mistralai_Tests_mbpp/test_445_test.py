import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_simple(self):
        self.assertTupleEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18)))
        self.assertTupleEqual(index_multiplication((0, 0, 0), (1, 2, 3)), ((0, 0, 0)))
        self.assertTupleEqual(index_multiplication((-1, 2, -3), (4, 5, 6)), ((-4, 10, -18)))

    def test_edge_and_boundary(self):
        self.assertTupleEqual(index_multiplication((1,), (2,)), ((2,)))
        self.assertTupleEqual(index_multiplication((1, 2), ()), ((1, 2)))
        self.assertTupleEqual(index_multiplication((1, 2, 3), (1, 1, 1)), ((1, 2, 3)))
        self.assertTupleEqual(index_multiplication((1, 2, 3), (0, 0, 0)), ((0, 0, 0)))

    def test_complex(self):
        self.assertTupleEqual(index_multiplication((1, 2, 3), (4, 5, 6, 7)), ((4, 10, 18, 21)))
        self.assertTupleEqual(index_multiplication((1, 2, 3), (4, 5, 6, 7, 8)), ((4, 10, 18, 21, 24)))
        self.assertTupleEqual(index_multiplication((1, 2, 3), (4, 5, 6, 7, 8, 9)), ((4, 10, 18, 21, 24, 27)))

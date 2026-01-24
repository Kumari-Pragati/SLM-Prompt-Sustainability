import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_typical_case(self):
        self.assertTupleEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18)))
        self.assertTupleEqual(index_multiplication((0, 0, 0), (1, 2, 3)), ((0, 0, 0)))
        self.assertTupleEqual(index_multiplication((-1, 2, -3), (4, 5, 6)), ((-4, 10, -18)))

    def test_edge_case_empty_input(self):
        self.assertIsInstance(index_multiplication((), ()), TypeError)
        self.assertIsInstance(index_multiplication((1), ()), TypeError)
        self.assertIsInstance(index_multiplication((), (1)), TypeError)

    def test_edge_case_single_input(self):
        self.assertTupleEqual(index_multiplication((1), (2,)), ((2,)))
        self.assertTupleEqual(index_multiplication((1,), (2)), ((2,)))
        self.assertTupleEqual(index_multiplication((1, 2), ()), ((0, 0)))

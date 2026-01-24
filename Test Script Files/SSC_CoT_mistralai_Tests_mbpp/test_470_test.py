import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_normal(self):
        self.assertTupleEqual(add_pairwise((1, 2, 3, 4)), (2, 3, 4, 5))
        self.assertTupleEqual(add_pairwise((5, 4, 3, 2)), (6, 5, 4, 3))

    def test_edge_cases(self):
        self.assertTupleEqual(add_pairwise((1, 2)), (3,))
        self.assertTupleEqual(add_pairwise((1, 2, 3)), (2, 3, 4))
        self.assertTupleEqual(add_pairwise((1, 2, 3, 4, 5)), (2, 3, 4, 5, 6))

    def test_boundary_cases(self):
        self.assertTupleEqual(add_pairwise((0, 0)), (0,))
        self.assertTupleEqual(add_pairwise((-1, 1)), (0,))
        self.assertTupleEqual(add_pairwise((1000000000000, 1)), (1000000000001,))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_pairwise(123)
        with self.assertRaises(TypeError):
            add_pairwise((1, 'a'))

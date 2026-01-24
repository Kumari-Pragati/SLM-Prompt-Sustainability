import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_simple(self):
        self.assertTupleEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (1, 3, 2))
        self.assertTupleEqual(tuple_modulo((7, 2, 3), (4, 5, 6)), (3, 2, 1))
        self.assertTupleEqual(tuple_modulo((1, 0, 2), (4, 5, 6)), (1, 0, 2))

    def test_edge_cases(self):
        self.assertTupleEqual(tuple_modulo((0, 0, 0), (1, 1, 1)), (0, 0, 0))
        self.assertTupleEqual(tuple_modulo((1, 0, -1), (1, 1, 1)), (0, 0, 0))
        self.assertTupleEqual(tuple_modulo((1, 2, 3), (0, 0, 0)), (1, 2, 3))

    def test_complex(self):
        self.assertTupleEqual(tuple_modulo((1000000000000000001, 1000000000000000002),
                                             (1000000000000000003, 1000000000000000004)),
                               (1, 3, 2))
        self.assertTupleEqual(tuple_modulo((-1000000000000000001, -1000000000000000002),
                                             (-1000000000000000003, -1000000000000000004)),
                               (1, 3, 2))

import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertTupleEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (3, 0, 1))
        self.assertTupleEqual(tuple_modulo((-1, 2, -3), (4, 5, 6)), (-3, 2, -3))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(tuple_modulo((0, 2, 0), (4, 5, 6)), (0, 2, 0))
        self.assertTupleEqual(tuple_modulo((1, 0, 3), (4, 5, 6)), (1, 5, 3))
        self.assertTupleEqual(tuple_modulo((1, 2, 0), (0, 0, 6)), (1, 2, 0))
        self.assertTupleEqual(tuple_modulo((0, 0, 0), (4, 5, 6)), (0, 0, 0))

    def test_negative_numbers(self):
        self.assertTupleEqual(tuple_modulo((-1, 2, -3), (-4, -5, -6)), (1, 7, 3))
        self.assertTupleEqual(tuple_modulo((1, -2, -3), (-4, -5, -6)), (-3, 7, -1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_modulo(123, (4, 5, 6))
        with self.assertRaises(TypeError):
            tuple_modulo((1, 2, 3), 456)

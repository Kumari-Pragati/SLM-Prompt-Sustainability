import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(tuple_modulo((5, 10), (2, 3)), (1, 1))
        self.assertEqual(tuple_modulo((10, 20), (5, 10)), (0, 0))

    def test_edge_conditions(self):
        self.assertEqual(tuple_modulo((0, 0), (1, 1)), (0, 0))
        self.assertEqual(tuple_modulo((1, 2), (0, 0)), (1, 2))

    def test_boundary_conditions(self):
        self.assertEqual(tuple_modulo((-1, 1), (1, 1)), (-1, 0))
        self.assertEqual(tuple_modulo((1, -1), (1, 1)), (0, -1))

    def test_complex_cases(self):
        self.assertEqual(tuple_modulo((10, 20), (5, 11)), (0, 9))
        self.assertEqual(tuple_modulo((-10, 20), (5, -11)), (-0, 9))

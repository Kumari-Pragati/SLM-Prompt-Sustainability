import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_modulo((10, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_edge_conditions(self):
        self.assertEqual(tuple_modulo((0, 0, 0), (1, 2, 3)), (0, 0, 0))
        self.assertEqual(tuple_modulo((1, 2, 3), (0, 0, 0)), (1, 2, 3))

    def test_boundary_conditions(self):
        self.assertEqual(tuple_modulo((-1, 0, 1), (1, 2, 3)), (-1, 0, 1))
        self.assertEqual(tuple_modulo((1, 2, 3), (-1, 0, 1)), (0, 1, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_modulo((1, 2, 3), 'a')
        with self.assertRaises(TypeError):
            tuple_modulo('a', (1, 2, 3))
        with self.assertRaises(TypeError):
            tuple_modulo('a', 'b')

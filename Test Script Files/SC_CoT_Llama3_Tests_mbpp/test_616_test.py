import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (1 % 4, 2 % 5, 3 % 6))

    def test_edge_cases(self):
        self.assertEqual(tuple_modulo((0, 0), (0, 0)), (0, 0))
        self.assertEqual(tuple_modulo((1, 2, 3), (0, 0, 0)), (1, 2, 3))

    def test_boundary_cases(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (10, 20, 30)), (1, 2, 3))
        self.assertEqual(tuple_modulo((10, 20, 30), (1, 2, 3)), (0, 0, 0))

    def test_special_cases(self):
        self.assertEqual(tuple_modulo((-1, 2, 3), (4, 5, 6)), (-1 % 4, 2 % 5, 3 % 6))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_modulo('test', (1, 2, 3))
        with self.assertRaises(TypeError):
            tuple_modulo((1, 2, 3), 'test')

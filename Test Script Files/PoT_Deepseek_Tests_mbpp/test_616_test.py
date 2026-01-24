import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((10, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_edge_case(self):
        self.assertEqual(tuple_modulo((0, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_boundary_case(self):
        self.assertEqual(tuple_modulo((1, 21, 31), (1, 11, 16)), (0, 0, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_modulo((10, 20, 30), 5)

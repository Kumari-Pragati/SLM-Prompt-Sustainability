import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((10, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_edge_case(self):
        self.assertEqual(tuple_modulo((0, 0, 0), (5, 10, 15)), (0, 0, 0))

    def test_boundary_case(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (0, 0, 0)), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_modulo((10, 20, 30), 5)

        with self.assertRaises(TypeError):
            tuple_modulo(10, (20, 30))

        with self.assertRaises(TypeError):
            tuple_modulo((10, 20, 'a'), (5, 10, 15))

        with self.assertRaises(TypeError):
            tuple_modulo((10, 20, 30.5), (5, 10, 15))

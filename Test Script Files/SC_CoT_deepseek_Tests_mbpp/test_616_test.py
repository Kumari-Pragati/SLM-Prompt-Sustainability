import unittest

from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((5, 3), (2, 7)), ((5 % 2, 3 % 7)))

    def test_boundary_case(self):
        self.assertEqual(tuple_modulo((0, 0), (0, 0)), ((0 % 0, 0 % 0)))

    def test_edge_case(self):
        self.assertEqual(tuple_modulo((1, 2), (0, 1)), ((1 % 0, 2 % 1)))

    def test_special_case(self):
        self.assertEqual(tuple_modulo((10, -5), (2, -2)), ((10 % 2, (-5) % (-2))))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_modulo((1, 2), 'a')

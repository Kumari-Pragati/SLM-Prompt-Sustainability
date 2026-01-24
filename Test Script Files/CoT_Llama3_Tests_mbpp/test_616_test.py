import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(tuple_modulo((10, 2, 3), (2, 3, 4)), (0, 1, 1))

    def test_edge_case(self):
        self.assertEqual(tuple_modulo((10, 2, 3), (2, 3, 0)), (0, 1, 3))

    def test_edge_case2(self):
        self.assertEqual(tuple_modulo((10, 2, 3), (0, 3, 4)), (10, 2, 1))

    def test_edge_case3(self):
        self.assertEqual(tuple_modulo((10, 2, 3), (0, 0, 4)), (10, 2, 3))

    def test_edge_case4(self):
        self.assertEqual(tuple_modulo((10, 2, 3), (0, 0, 0)), (10, 2, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_modulo('test', (2, 3, 4))

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            tuple_modulo((10, 2, 3), 'test')

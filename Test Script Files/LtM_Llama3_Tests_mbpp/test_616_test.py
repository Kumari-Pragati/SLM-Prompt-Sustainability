import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (1, 2, 3)), (0, 0, 0))
    def test_empty_input(self):
        with self.assertRaises(TypeError):
            tuple_modulo([], [1, 2, 3])
    def test_empty_input2(self):
        with self.assertRaises(TypeError):
            tuple_modulo([1, 2, 3], [])
    def test_single_element(self):
        self.assertEqual(tuple_modulo((1,), (2,)), (1,))
    def test_single_element2(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (2,)), (1, 1, 1))
    def test_negative_numbers(self):
        self.assertEqual(tuple_modulo((-1, 2, 3), (2, 3, 4)), (-1, 2, 3))
    def test_large_numbers(self):
        self.assertEqual(tuple_modulo((1000000, 2, 3), (2, 3, 4)), (0, 2, 3))
    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            tuple_modulo((1, 'a', 3.0), (2, 3, 4))

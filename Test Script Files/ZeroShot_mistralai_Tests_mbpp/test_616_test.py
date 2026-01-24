import unittest
from616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_simple_tuples(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (3, 0, 3))
        self.assertEqual(tuple_modulo((-1, 2, -3), (4, 5, 6)), (-1, 2, -3))
        self.assertEqual(tuple_modulo((0, 0, 0), (4, 5, 6)), (0, 0, 0))

    def test_mixed_tuples(self):
        self.assertEqual(tuple_modulo((1, 0, 3), (4, 0, 6)), (1, 0, 3))
        self.assertEqual(tuple_modulo((-1, 0, -3), (4, 0, 6)), (-1, 0, -3))
        self.assertEqual(tuple_modulo((0, 0, 0), (4, 0, 6)), (0, 0, 0))

    def test_empty_tuples(self):
        self.assertEqual(tuple_modulo((), (4, 5, 6)), ())
        self.assertEqual(tuple_modulo((4, 5, 6),()), ())
        self.assertEqual(tuple_modulo((),()), ())

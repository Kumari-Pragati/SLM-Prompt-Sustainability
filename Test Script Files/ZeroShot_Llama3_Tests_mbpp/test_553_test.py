import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(tuple_to_float((1, 2, 3)), 1.2)
        self.assertEqual(tuple_to_float((4, 5, 6)), 4.5)
        self.assertEqual(tuple_to_float((7, 8, 9)), 7.8)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float('abc')
        with self.assertRaises(TypeError):
            tuple_to_float([1, 2, 3])
        with self.assertRaises(TypeError):
            tuple_to_float({'a': 1, 'b': 2, 'c': 3})

    def test_edge_cases(self):
        self.assertEqual(tuple_to_float(()), 0.0)
        self.assertEqual(tuple_to_float((1,)), 1.0)
        self.assertEqual(tuple_to_float((1, 2)), 1.2)

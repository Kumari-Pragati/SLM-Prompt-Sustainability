import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), ((6, 8), (10, 12)))

    def test_edge_cases(self):
        self.assertEqual(add_nested_tuples(((1, 2),), ((3, 4),)), ((4, 6),))
        self.assertEqual(add_nested_tuples(((1, 2),), ()), ())
        self.assertEqual(add_nested_tuples((), ((3, 4),)), ())
        self.assertEqual(add_nested_tuples(((1, 2),), None), ())
        self.assertEqual(add_nested_tuples(None, ((3, 4),)), ())

    def test_special_cases(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4), (5, 6)), ((7, 8), (9, 10), (11, 12))), ((8, 10, 12), (14, 16, 18)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_nested_tuples('test_tup1', 'test_tup2')
        with self.assertRaises(TypeError):
            add_nested_tuples(None, None)

import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), (((6, 8),),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6),)), (((6, 4),)))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5,), (6, 7))), (((6, 7),)))

    def test_edge_cases(self):
        self.assertEqual(add_nested_tuples(((1, 2),), ((3, 4),)), (((3, 4),)))
        self.assertEqual(add_nested_tuples(((1, 2),), ((3, 4), (5, 6))), (((3, 4), (5, 6)),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((), (5, 6))), (((3, 4),),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), ())), (((3, 4), (5, 6)),))
        self.assertEqual(add_nested_tuples(((1, 2),), ((),)), (((),)))
        self.assertEqual(add_nested_tuples(((1, 2),), ((), ())), (((),)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), (3, 4))
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), "3")
        self.assertRaises(TypeError, add_nested_tuples, "1", (2, 3))

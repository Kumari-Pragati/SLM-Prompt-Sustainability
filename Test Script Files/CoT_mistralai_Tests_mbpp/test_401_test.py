import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ())

    def test_single_level_tuples(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((1 + 3, 2 + 4)))
        self.assertEqual(add_nested_tuples((1, 2), (3,)), ((1 + 3, 2)))
        self.assertEqual(add_nested_tuples((1,), (3, 4)), ((1 + 3, 4)))

    def test_multi_level_tuples(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), (((5, 6), (7, 8)),)),
                         (((1 + 5, 2 + 6), (3 + 7, 4 + 8))))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), (((5,), (7, 8)),)),
                         (((1 + 5, 2), (3 + 7, 8))))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((((5,),), ((7, 8),)),)),
                         (((1 + 5, 2), (3, 7 + 8))))

    def test_mixed_level_tuples(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))),
                         (((1 + 5, 2 + 6), (3 + 7, 4 + 8))))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5,), (7, 8))),
                         (((1 + 5, 2), (3 + 7, 8))))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6),)),
                         (((1 + 5, 2 + 6), (3, 4))))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), 'abc')
        self.assertRaises(TypeError, add_nested_tuples, 'abc', (1, 2))
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), (1, 2, 3))

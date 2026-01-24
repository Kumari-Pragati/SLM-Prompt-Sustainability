import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), ((((6, 8),), (10, 12)),))

    def test_edge_cases(self):
        self.assertEqual(add_nested_tuples((), ()), ())
        self.assertEqual(add_nested_tuples((1,), ()), ((1,),))
        self.assertEqual(add_nested_tuples(((), (1,)), ((1,), ())) , (((1,),),))
        self.assertEqual(add_nested_tuples(((), (1, 2)), ((1,), (3, 4))), ((((1, 3),), (2, 4)),))

    def test_complex(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8, 9))), ((((6, 8, 9),), (1 + 5, 2 + 7)),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6, 7), (8, 9))), ((((6, 8, 9),), (1 + 5, 2 + 7)), ((3 + 8, 4 + 9)),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8, 9), (10, 11))), ((((6, 8, 9, 10, 11),), (1 + 5, 2 + 7)), ((3 + 8, 4 + 9)),))

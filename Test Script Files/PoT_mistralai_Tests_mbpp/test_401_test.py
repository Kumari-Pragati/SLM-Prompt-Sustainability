import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), (((5, 6), (7, 8)),)), (((6, 8), (10, 12)),))
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), (((6, 8),), (1, 9)))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ((),))
        self.assertEqual(add_nested_tuples((1,), (2,)), ((3,),))
        self.assertEqual(add_nested_tuples((1,), ((2,),)), (((3,),),))

    def test_edge_case_single_tuple(self):
        self.assertEqual(add_nested_tuples((1, 2), ()), ((2,),))
        self.assertEqual(add_nested_tuples((), (1, 2)), ((2,),))

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), (3, '4'))
        self.assertRaises(TypeError, add_nested_tuples, (1, 2), (3, [4]))

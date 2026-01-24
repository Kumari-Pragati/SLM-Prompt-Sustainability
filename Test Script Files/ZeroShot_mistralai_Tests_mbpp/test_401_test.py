import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(add_nested_tuples((1,), (2,)), (3,))
        self.assertEqual(add_nested_tuples((2,), (1,)), (3,))

    def test_multiple_element_tuples(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), (((6, 8), (7, 9)), ((3, 4), (5, 6))))
        self.assertEqual(add_nested_tuples(((3, 4), (5, 6)), ((1, 2), (7, 8))), (((4, 6), (5, 8)), ((3, 2), (7, 6))))

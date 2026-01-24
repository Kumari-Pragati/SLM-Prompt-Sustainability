import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ())
        self.assertEqual(add_nested_tuples((1, 2), ()), ((1, 2),))
        self.assertEqual(add_nested_tuples((1, 2), (3,)), ((1, 2), (3,)))

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(add_nested_tuples((1,), (2,)), ((3,),))
        self.assertEqual(add_nested_tuples((1, 2), (3,)), ((4, 5),))

    def test_edge_case_single_element_tuples_empty(self):
        self.assertEqual(add_nested_tuples((1,), ()), ((1,),))
        self.assertEqual(add_nested_tuples((1,), (2,)), ((3,),))

    def test_edge_case_single_element_tuples_single_element(self):
        self.assertEqual(add_nested_tuples((1,), (1,)), ((2,),))

    def test_edge_case_single_element_tuples_single_element_empty(self):
        self.assertEqual(add_nested_tuples((1,), ()), ((1,),))

    def test_edge_case_single_element_tuples_single_element_single_element(self):
        self.assertEqual(add_nested_tuples((1,), (1,)), ((2,),))

    def test_edge_case_single_element_tuples_single_element_single_element_empty(self):
        self.assertEqual(add_nested_tuples((1,), (1,)), ((2,),))

import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_nested_tuples((1, 2), (3, 4)), ((4, 6),))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(add_nested_tuples((), ()), ((),))

    def test_edge_case_single_tuple(self):
        self.assertEqual(add_nested_tuples((1, 2), ()), ((1, 2),))

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(add_nested_tuples((1,), (2,)), ((3,),))

    def test_edge_case_zero_length_tuples(self):
        self.assertEqual(add_nested_tuples((), (1, 2)), (()))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(add_nested_tuples((-1, 2), (-3, 4)), ((-4, 6),))

    def test_edge_case_non_integer_numbers(self):
        self.assertEqual(add_nested_tuples((1.0, 2.0), (3.0, 4.0)), ((4.0, 6.0),))

    def test_edge_case_mixed_types(self):
        self.assertEqual(add_nested_tuples((1, 'a'), (2, 'b')), ((3, 'ab'),))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            add_nested_tuples(1, (2, 3))

    def test_error_case_non_tuple_input2(self):
        with self.assertRaises(TypeError):
            add_nested_tuples((1, 2), 'abc')

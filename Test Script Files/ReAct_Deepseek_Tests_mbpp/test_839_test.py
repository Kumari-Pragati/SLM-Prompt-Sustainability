import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_case(self):
        tup = (('b', 2), ('a', 1), ('c', 3))
        expected_output = (('a', 1), ('b', 2), ('c', 3))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_edge_case_with_same_first_elements(self):
        tup = (('b', 2), ('b', 1), ('c', 3))
        expected_output = (('b', 1), ('b', 2), ('c', 3))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_edge_case_with_empty_tuples(self):
        tup = ()
        expected_output = ()
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_edge_case_with_single_tuple(self):
        tup = (('a', 1),)
        expected_output = (('a', 1),)
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_error_case_with_non_tuple_input(self):
        with self.assertRaises(TypeError):
            sort_tuple('a')

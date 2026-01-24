import unittest

from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_case(self):
        tup = (('b', 2), ('a', 1), ('c', 3))
        expected_output = (('a', 1), ('b', 2), ('c', 3))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_edge_case(self):
        tup = (('b', 2), ('b', 1), ('c', 3))
        expected_output = (('b', 1), ('b', 2), ('c', 3))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_single_element(self):
        tup = (('a', 1),)
        expected_output = (('a', 1),)
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_empty_tuple(self):
        tup = ()
        expected_output = ()
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple('not a tuple')

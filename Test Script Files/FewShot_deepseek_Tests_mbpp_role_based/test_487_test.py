import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_typical_use_case(self):
        tup = (('b', 2), ('a', 1), ('c', 3))
        expected_output = (('c', 3), ('b', 2), ('a', 1))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_edge_case(self):
        tup = (('b', 2), ('a', 2))
        expected_output = (('b', 2), ('a', 2))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_boundary_case(self):
        tup = (('b', 2), ('a', 2), ('c', 2))
        expected_output = (('c', 2), ('b', 2), ('a', 2))
        self.assertEqual(sort_tuple(tup), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(123)

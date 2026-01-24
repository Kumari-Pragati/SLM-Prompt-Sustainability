import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_single_tuple(self):
        self.assertEqual(join_tuples([("a", "b", "c")]), [("a", "b", "c")])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([("a", "b", "c"), ("a", "d", "e"), ("f", "g", "h")]), [("a", "b", "c"), ("a", "d", "e"), ("f", "g", "h")])

    def test_merging_tuples(self):
        self.assertEqual(join_tuples([("a", "b", "c"), ("a", "b", "d"), ("e", "f", "g")]), [("a", "b", "c", "d"), ("e", "f", "g")])

    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple_in_list(self):
        self.assertEqual(join_tuples([("a", "b", "c")]), [("a", "b", "c")])

    def test_multiple_tuples_with_duplicates(self):
        self.assertEqual(join_tuples([("a", "b", "c"), ("a", "b", "d"), ("a", "e", "f")]), [("a", "b", "c", "d", "e", "f")])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            join_tuples("invalid_input")

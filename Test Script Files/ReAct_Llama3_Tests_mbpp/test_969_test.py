import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([("a",)]), [("a",)])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([("a",), ("b",), ("c",)]), [("a",), ("b",), ("c",)])

    def test_merged_tuples(self):
        self.assertEqual(join_tuples([("a",), ("a", "b"), ("c",)]), [("a",), ("b",), ("c",)])

    def test_merged_tuples_with_duplicates(self):
        self.assertEqual(join_tuples([("a",), ("a", "b"), ("a", "c"), ("d",)]), [("a",), ("b",), ("c",), ("d",)])

    def test_empty_tuple(self):
        self.assertEqual(join_tuples([()]), [()])

    def test_single_empty_tuple(self):
        self.assertEqual(join_tuples([("a",), ()]), [("a",)])

    def test_multiple_empty_tuples(self):
        self.assertEqual(join_tuples([(), (), ()]), [(), (), ()])

    def test_merged_empty_tuples(self):
        self.assertEqual(join_tuples([(), ("a",), ()]), [(), ("a",), ()])

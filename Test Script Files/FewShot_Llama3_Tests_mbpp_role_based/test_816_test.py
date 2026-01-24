import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        test_tup = ()
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_non_empty_tuple(self):
        test_tup = (1, 2, 3)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_duplicates(self):
        test_tup = (1, 2, 2, 3, 3, 3)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_mixed_types(self):
        test_tup = (1, "hello", 3.14, None)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_nested_tuples(self):
        test_tup = ((1, 2), (3, 4), (5, 6))
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_empty_list(self):
        test_tup = ([1, 2, 3],)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

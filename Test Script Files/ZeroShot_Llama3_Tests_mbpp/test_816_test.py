import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_empty_tuple(self):
        test_tup = ()
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_single_element_tuple(self):
        test_tup = (1,)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_multiple_elements_tuple(self):
        test_tup = (1, 2, 3)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_duplicates(self):
        test_tup = (1, 2, 2, 3, 3, 3)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_empty_string(self):
        test_tup = ("", "hello", "world")
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_empty_string_and_duplicates(self):
        test_tup = ( "", "hello", "world", "", "hello", "world")
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_typical_case(self):
        test_tup = (1, 2, 3)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_empty_input(self):
        test_tup = ()
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_single_element_input(self):
        test_tup = (4,)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_multiple_element_input(self):
        test_tup = (5, 6, 7)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_duplicates(self):
        test_tup = (8, 8, 8)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_negative_numbers(self):
        test_tup = (-9, -10, -11)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

    def test_tuple_with_mixed_types(self):
        test_tup = (12, "hello", 13.5)
        result = clear_tuple(test_tup)
        self.assertEqual(result, ())

import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3, 4, 5)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_empty_tuple(self):
        test_tup = ()
        self.assertEqual(clear_tuple(test_tup), ())

    def test_single_element_tuple(self):
        test_tup = (1,)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_large_tuple(self):
        test_tup = tuple(range(1, 1001))
        self.assertEqual(clear_tuple(test_tup), ())

    def test_tuple_with_duplicates(self):
        test_tup = (1, 2, 2, 3, 4, 4, 5)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_tuple_with_negative_numbers(self):
        test_tup = (-1, -2, -3, -4, -5)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_tuple_with_zero(self):
        test_tup = (0, 1, 2, 3, 4)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_tuple_with_mixed_types(self):
        test_tup = (1, 'two', 3.0, 'four', 5)
        self.assertEqual(clear_tuple(test_tup), ())

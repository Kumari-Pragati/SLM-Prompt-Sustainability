import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_clear_tuple_with_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_clear_tuple_with_non_empty_tuple(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_clear_tuple_with_single_element_tuple(self):
        self.assertEqual(clear_tuple((1,)), ())

    def test_clear_tuple_with_duplicate_elements(self):
        self.assertEqual(clear_tuple((1, 1, 2, 2)), ())

    def test_clear_tuple_with_negative_numbers(self):
        self.assertEqual(clear_tuple((-1, -2, -3)), ())

    def test_clear_tuple_with_zero(self):
        self.assertEqual(clear_tuple((0,)), ())

import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(clear_tuple((1,)), ())

    def test_multiple_elements_tuple(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_tuple_with_duplicates(self):
        self.assertEqual(clear_tuple((1, 1, 2, 2, 3, 3)), ())

    def test_tuple_with_empty_list(self):
        self.assertEqual(clear_tuple(()), ())

    def test_tuple_with_non_empty_list(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_tuple_with_mixed_types(self):
        self.assertEqual(clear_tuple((1, 'a', 2.5)), ())

    def test_tuple_with_mixed_types_and_duplicates(self):
        self.assertEqual(clear_tuple((1, 'a', 2.5, 1, 'a', 2.5)), ())

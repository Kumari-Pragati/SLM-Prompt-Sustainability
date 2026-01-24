import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_empty_set(self):
        self.assertEqual(set_to_tuple(set()), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({1}), (1,))

    def test_multiple_elements_set(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))

    def test_set_with_duplicates(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 2, 3}), (1, 2, 3))

    def test_set_with_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, 0, 1}), (-1, 0, 1))

    def test_set_with_non_integer_elements(self):
        self.assertEqual(set_to_tuple({1.0, 2.0, 3.0}), (1.0, 2.0, 3.0))

    def test_set_with_mixed_types(self):
        self.assertEqual(set_to_tuple({1, 2, 'a', 'b'}), ('a', 'b', 1, 2))

    def test_set_with_empty_string(self):
        self.assertEqual(set_to_tuple({'', 'a'}), ('', 'a'))

    def test_set_with_none(self):
        self.assertEqual(set_to_tuple({None}), (None,))

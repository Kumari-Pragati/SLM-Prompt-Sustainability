import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({'a', 'b', 'c'}), ('a', 'b', 'c'))

    def test_empty_input(self):
        self.assertEqual(set_to_tuple({}), ())
        self.assertEqual(set_to_tuple({None}), ())

    def test_single_input(self):
        self.assertEqual(set_to_tuple({1}), (1,))
        self.assertEqual(set_to_tuple({'a'}), ('a',))

    def test_duplicate_input(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 3}), (1, 1, 2, 3))
        self.assertEqual(set_to_tuple({'a', 'a', 'b', 'c'}), ('a', 'a', 'b', 'c'))

    def test_sorted_order(self):
        self.assertEqual(set_to_tuple({3, 1, 2}), (1, 2, 3))
        self.assertEqual(set_to_tuple({'z', 'a', 'b'}), ('a', 'b', 'z'))

    def test_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, 0, 1}), (-1, 0, 1))

    def test_mixed_types(self):
        self.assertEqual(set_to_tuple({1, 'a', 2.5}), (1, 'a', 2.5))

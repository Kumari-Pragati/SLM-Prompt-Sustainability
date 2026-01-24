import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))
        self.assertEqual(set_toTuple({'a', 'b', 'c'}), ('a', 'b', 'c'))

    def test_edge_case_empty_set(self):
        self.assertEqual(set_toTuple({}), ())

    def test_edge_case_single_element(self):
        self.assertEqual(set_toTuple({1}), (1,))
        self.assertEqual(set_toTuple({'a'}), ('a',))

    def test_edge_case_duplicates(self):
        self.assertEqual(set_toTuple({1, 1}), (1,))
        self.assertEqual(set_toTuple({'a', 'a'}), ('a',))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(set_toTuple({-1, 0, 1}), (-1, 0, 1))

    def test_corner_case_mixed_types(self):
        self.assertEqual(set_toTuple({1, 'a', 3.14}), (1, 'a', 3.14))

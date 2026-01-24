import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):
    def test_empty_set(self):
        self.assertEqual(set_to_tuple({}), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({1}), (1,))

    def test_multiple_elements_set(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))

    def test_duplicate_elements_set(self):
        self.assertEqual(set_to_tuple({1, 2, 2, 3}), (1, 2, 3))

    def test_mixed_types_set(self):
        self.assertEqual(set_to_tuple({1, "a", 2.5}), (1, "a", 2.5))

    def test_set_with_none(self):
        self.assertEqual(set_to_tuple({None}), (None,))

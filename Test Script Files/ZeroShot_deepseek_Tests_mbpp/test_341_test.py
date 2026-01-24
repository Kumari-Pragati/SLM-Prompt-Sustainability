import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_empty_set(self):
        self.assertEqual(set_to_tuple(set()), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({1}), (1,))

    def test_multiple_elements_set(self):
        self.assertEqual(set_to_tuple({3, 2, 1}), (1, 2, 3))

    def test_duplicate_elements_set(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 2}), (1, 2))

    def test_non_integer_elements_set(self):
        self.assertEqual(set_to_tuple({'a', 'b', 'c'}), ('a', 'b', 'c'))

    def test_mixed_integer_string_set(self):
        self.assertEqual(set_to_tuple({1, 'a', 2, 'b'}), ('1', '2', 'a', 'b'))

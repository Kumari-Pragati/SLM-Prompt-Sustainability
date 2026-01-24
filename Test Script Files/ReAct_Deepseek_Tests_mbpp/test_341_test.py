import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))

    def test_empty_set(self):
        self.assertEqual(set_to_tuple(set()), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({42}), (42,))

    def test_duplicate_elements(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 2}), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, -2, -3}), (-3, -2, -1))

    def test_sorted_set(self):
        self.assertEqual(set_to_tuple({3, 2, 1}), (1, 2, 3))

    def test_large_set(self):
        self.assertEqual(set_to_tuple(set(range(1000))), tuple(range(1000)))

    def test_non_integer_elements(self):
        self.assertEqual(set_to_tuple({1.1, 2.2, 3.3}), (1.1, 2.2, 3.3))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            set_to_tuple({1, 'two', 3.0})

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
        self.assertEqual(set_to_tuple({1, 1, 2, 3}), (1, 2, 3))

    def test_set_with_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, 0, 1}), (-1, 0, 1))

    def test_set_with_floating_point_numbers(self):
        self.assertEqual(set_to_tuple({1.0, 2.0}), (1.0, 2.0))

    def test_set_with_mixed_types(self):
        with self.assertRaises(TypeError):
            set_to_tuple([1, 2, 3])

    def test_set_with_non_hashable_types(self):
        with self.assertRaises(TypeError):
            set_to_tuple({1, 2, "a"})

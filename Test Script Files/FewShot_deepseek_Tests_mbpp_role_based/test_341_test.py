import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))

    def test_empty_set(self):
        self.assertEqual(set_to_tuple({}), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({1}), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(set_to_tuple({1, 2, 2}), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, -2, -3}), (-3, -2, -1))

    def test_mixed_numbers(self):
        self.assertEqual(set_to_tuple({1, -1, 2, -2}), (-2, -1, 1, 2))

    def test_non_integer_elements(self):
        self.assertEqual(set_to_tuple({1.5, 2.5, 3.5}), (1.5, 2.5, 3.5))

    def test_non_unique_elements(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 2}), (1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            set_to_tuple("1, 2, 3")

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

    def test_set_with_zero(self):
        self.assertEqual(set_to_tuple({0}), (0,))

    def test_set_with_negative_and_positive_numbers(self):
        self.assertEqual(set_to_tuple({-1, 0, 1}), (-1, 0, 1))

    def test_set_with_empty_list(self):
        with self.assertRaises(TypeError):
            set_to_tuple([])

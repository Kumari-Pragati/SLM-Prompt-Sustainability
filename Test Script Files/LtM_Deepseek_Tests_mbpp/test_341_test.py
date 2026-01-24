import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))

    def test_empty_set(self):
        self.assertEqual(set_to_tuple(set()), ())

    def test_single_element_set(self):
        self.assertEqual(set_to_tuple({4}), (4,))

    def test_duplicate_elements(self):
        self.assertEqual(set_to_tuple({1, 2, 2}), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(set_to_tuple({-1, -2, -3}), (-3, -2, -1))

    def test_mixed_numbers(self):
        self.assertEqual(set_to_tuple({1, -1, 2, -2}), (-2, -1, 1, 2))

    def test_large_numbers(self):
        self.assertEqual(set_to_tuple({100, 200, 300}), (100, 200, 300))

    def test_large_set(self):
        self.assertEqual(set_to_tuple(set(range(1, 101))), tuple(range(1, 101)))

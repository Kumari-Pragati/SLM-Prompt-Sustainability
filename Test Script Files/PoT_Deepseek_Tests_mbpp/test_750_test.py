import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_tuple([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(add_tuple([], (3, 4)), [3, 4])

    def test_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2], ()), [1, 2])

    def test_single_element_tuple(self):
        self.assertEqual(add_tuple([1, 2], (3,)), [1, 2, 3])

    def test_single_element_list(self):
        self.assertEqual(add_tuple([1], (3, 4)), [1, 3, 4])

    def test_large_numbers(self):
        self.assertEqual(add_tuple([1000, 2000], (3000, 4000)), [1000, 2000, 3000, 4000])

    def test_negative_numbers(self):
        self.assertEqual(add_tuple([-1, -2], (-3, -4)), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        self.assertEqual(add_tuple([1, -2], (3, -4)), [1, -2, 3, -4])

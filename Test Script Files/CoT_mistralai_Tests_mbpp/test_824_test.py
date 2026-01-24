import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], remove_even([]))

    def test_single_element(self):
        self.assertListEqual([1], remove_even([1]))
        self.assertListEqual([2], remove_even([2]))

    def test_even_length(self):
        self.assertListEqual([1, 3], remove_even([0, 1, 2, 3, 4, 5]))
        self.assertListEqual([2, 4, 6], remove_even([1, 2, 3, 4, 5, 6]))

    def test_odd_length(self):
        self.assertListEqual([1, 3, 5], remove_even([0, 1, 2, 3, 4, 5, 6]))
        self.assertListEqual([1, 3, 5, 7], remove_even([0, 1, 2, 3, 4, 5, 6, 7]))

    def test_negative_numbers(self):
        self.assertListEqual([1, 3], remove_even([-2, -1, 0, 1, 2, 3]))
        self.assertListEqual([-1, 1], remove_even([-2, -1, 0, 1]))

    def test_floats(self):
        self.assertListEqual([1.5, 3.5], remove_even([0.0, 1.5, 2.0, 3.5]))
        self.assertListEqual([2.0], remove_even([1.0, 2.0]))

    def test_mixed_types(self):
        self.assertListEqual([1, 3], remove_even([0, 1, "two", 3]))
        self.assertListEqual([], remove_even([0, "one", 2]))

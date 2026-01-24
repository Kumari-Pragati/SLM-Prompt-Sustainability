import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], remove_odd([]))

    def test_single_even_element(self):
        self.assertListEqual([2], remove_odd([2]))

    def test_single_odd_element(self):
        self.assertListEqual([], remove_odd([1]))

    def test_mixed_list(self):
        self.assertListEqual([2, 4, 6], remove_odd([1, 2, 3, 4, 5, 6]))

    def test_only_odd_list(self):
        self.assertListEqual([], remove_odd([1, 3, 5]))

    def test_negative_numbers(self):
        self.assertListEqual([-2, -4], remove_odd([-1, -2, -3, -4]))

    def test_floating_point_numbers(self):
        self.assertListEqual([2.0], remove_odd([1.5, 2.0, 3.5]))

    def test_mixed_types(self):
        self.assertListEqual([2, 'a', 4], remove_odd([1, 2, 'a', 3, 4]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_odd, (1, 2, 3))

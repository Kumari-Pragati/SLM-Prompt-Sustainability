import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(re_arrange([1, 2, 3, -4, 5, -6, 7, -8], 8), [1, -4, 3, 2, 5, -6, -8, 7])
        self.assertEqual(re_arrange([-1, 0, 1, -2, 3, -4, 5, -6], 8), [-1, 0, -2, 1, -4, 3, -6, 5])

    def test_negative_numbers(self):
        self.assertEqual(re_arrange([-1, -2, -3, 4, -5, 6, -7, 8], 8), [-1, 4, -3, -2, 6, -7, 8, -5])
        self.assertEqual(re_arrange([8, 7, -6, -5, 6, -7, 1, -2], 8), [8, 1, -6, 7, -5, -2, -7, 6])

    def test_empty_list(self):
        self.assertEqual(re_arrange([], 8), [])

    def test_single_element_list(self):
        self.assertEqual(re_arrange([1], 1), [1])

    def test_odd_length_list(self):
        self.assertEqual(re_arrange([1, 2, 3], 3), [1, 2, 3])

    def test_even_length_list(self):
        self.assertEqual(re_arrange([1, 2], 2), [1, 2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            re_arrange('string', 8)
        with self.assertRaises(TypeError):
            re_arrange([1, 2, 3], 'string')
        with self.assertRaises(ValueError):
            re_arrange([], -1)
        with self.assertRaises(ValueError):
            re_arrange([1], -1)

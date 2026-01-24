import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_empty_lists(self):
        self.assertEqual(sub_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(sub_list([1], [2]), [-1])

    def test_negative_numbers(self):
        self.assertEqual(sub_list([1, -2, 3], [4, 5, -6]), [-3, -7, 9])

    def test_different_lengths(self):
        self.assertEqual(sub_list([1, 2, 3, 4], [5, 6]), [-4, -4])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], 'a')
        with self.assertRaises(TypeError):
            sub_list('a', [1, 2, 3])
        with self.assertRaises(TypeError):
            sub_list('a', 'b')

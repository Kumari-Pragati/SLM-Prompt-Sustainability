import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(mul_list([2], [3]), [6])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, -3], [4, -5, 6]), [-4, -10, -18])

    def test_zero_in_lists(self):
        self.assertEqual(mul_list([1, 2, 3], [0, 5, 0]), [0, 10, 0])

    def test_different_lengths(self):
        self.assertEqual(mul_list([1, 2, 3, 4], [5, 6]), [5, 12, 18])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], ['a', 'b', 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            mul_list('123', [1, 2, 3])

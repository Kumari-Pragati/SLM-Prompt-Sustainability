import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(add_list([]), [])
        self.assertListEqual(add_list([], [1, 2, 3]), [1, 2, 3])
        self.assertListEqual(add_list([1, 2, 3], []), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertListEqual(add_list([1], [2]), [3])
        self.assertListEqual(add_list([2], [1]), [3])

    def test_same_length_lists(self):
        self.assertListEqual(add_list([1, 2], [3, 4]), [4, 6])
        self.assertListEqual(add_list([3, 4], [1, 2]), [4, 6])

    def test_different_length_lists(self):
        self.assertListEqual(add_list([1, 2], [3]), [4, 2])
        self.assertListEqual(add_list([3], [1, 2]), [4, 2])

    def test_negative_numbers(self):
        self.assertListEqual(add_list([-1, 2], [-3, 4]), [1, 6])
        self.assertListEqual(add_list([-3, 4], [-1, 2]), [1, 6])

    def test_zero(self):
        self.assertListEqual(add_list([0], [1, 2]), [1, 2])
        self.assertListEqual(add_list([1, 2], [0]), [1, 2])
        self.assertListEqual(add_list([0], [0]), [0])

    def test_float_numbers(self):
        self.assertAlmostEqual(add_list([1.5, 2.5], [3.5, 4.5]), [5.0, 7.0])
        self.assertAlmostEqual(add_list([3.5, 4.5], [1.5, 2.5]), [5.0, 7.0])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            add_list('a', 'b')
        with self.assertRaises(TypeError):
            add_list([1], [2, 'c'])

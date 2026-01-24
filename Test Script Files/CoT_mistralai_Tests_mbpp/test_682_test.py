import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([], [1, 2, 3]), [])
        self.assertEqual(mul_list([1, 2, 3], []), [])

    def test_single_element_lists(self):
        self.assertEqual(mul_list([1], [2, 3]), [2, 3])
        self.assertEqual(mul_list([2, 3], [1]), [2, 3])
        self.assertEqual(mul_list([1], [1]), [1])

    def test_equal_length_lists(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertEqual(mul_list([4, 5, 6], [1, 2, 3]), [4, 10, 18])

    def test_different_length_lists(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5]), [4, 10, 15])
        self.assertEqual(mul_list([4, 5], [1, 2, 3]), [4, 10, 15])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, -3], [4, -5, 6]), [-4, 4, -18])
        self.assertEqual(mul_list([4, -5, 6], [-1, 2, -3]), [-4, 4, -18])

    def test_floats(self):
        self.assertListEqual(mul_list([1.5, 2.5], [3, 4]), [4.5, 6])
        self.assertListEqual(mul_list([3, 4], [1.5, 2.5]), [4.5, 6])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            mul_list('str', [1, 2, 3])
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], 'str')

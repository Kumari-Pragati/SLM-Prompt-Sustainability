import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element(self):
        self.assertEqual(get_inv_count([1], 1), 0)
        self.assertEqual(get_inv_count([0], 1), 0)

    def test_simple_list(self):
        self.assertEqual(get_inv_count([1, 0, 1], 3), 1)
        self.assertEqual(get_inv_count([0, 1, 2], 3), 2)
        self.assertEqual(get_inv_count([2, 1, 0], 3), 2)

    def test_reverse_list(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 5)

    def test_duplicates(self):
        self.assertEqual(get_inv_count([1, 1, 0], 3), 1)
        self.assertEqual(get_inv_count([0, 0, 1], 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, 0, 1], 3), 1)
        self.assertEqual(get_inv_count([1, -1, 0], 3), 1)
        self.assertEqual(get_inv_count([-1, -2, -3], 3), 3)

    def test_large_numbers(self):
        self.assertEqual(get_inv_count([1000000, 999999, 1], 3), 1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_inv_count([1, 0, 1], 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_inv_count(1, 2)
        with self.assertRaises(TypeError):
            get_inv_count([1], '2')

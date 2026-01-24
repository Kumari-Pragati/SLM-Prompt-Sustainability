import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 4), [4, 8, 12])

    def test_edge_case_zero(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [])

    def test_edge_case_negative(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 4), [-4, -8, -12])

    def test_edge_case_single_element(self):
        self.assertEqual(ntimes_list([5], 2), [10])

    def test_edge_case_empty_list(self):
        self.assertEqual(ntimes_list([], 3), [])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            ntimes_list([1, 2, 3], 'a')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            ntimes_list('a', 4)

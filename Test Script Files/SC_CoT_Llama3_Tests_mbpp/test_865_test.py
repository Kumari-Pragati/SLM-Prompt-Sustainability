import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(ntimes_list([1, 2, 3], 4), [4, 8, 12])

    def test_edge_case_zero(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_edge_case_negative(self):
        self.assertEqual(ntimes_list([1, 2, 3], -1), [-1, -2, -3])

    def test_edge_case_single_element(self):
        self.assertEqual(ntimes_list([5], 2), [10])

    def test_edge_case_empty_list(self):
        self.assertEqual(ntimes_list([], 3), [])

    def test_edge_case_single_element_zero(self):
        self.assertEqual(ntimes_list([0], 2), [0])

    def test_edge_case_single_element_negative(self):
        self.assertEqual(ntimes_list([-1], 2), [-2])

    def test_edge_case_single_element_zero(self):
        self.assertEqual(ntimes_list([0], 0), [])

    def test_edge_case_single_element_negative(self):
        self.assertEqual(ntimes_list([-1], 0), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ntimes_list('abc', 2)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            ntimes_list([1, 2, 3], 'abc')

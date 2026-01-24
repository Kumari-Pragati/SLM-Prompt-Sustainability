import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_edge_case_zero(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [])

    def test_edge_case_negative(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_edge_case_single_element(self):
        self.assertEqual(ntimes_list([5], 3), [15])

    def test_edge_case_empty_list(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ntimes_list("hello", 2)

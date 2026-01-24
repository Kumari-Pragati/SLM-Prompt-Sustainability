import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_edge_case_with_zero(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_boundary_case_with_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_boundary_case_with_large_numbers(self):
        self.assertEqual(ntimes_list([1000000000, 2000000000, 3000000000], 2), [2000000000, 4000000000, 6000000000])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            ntimes_list("1, 2, 3", 2)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            ntimes_list([1, 2, "3"], 2)

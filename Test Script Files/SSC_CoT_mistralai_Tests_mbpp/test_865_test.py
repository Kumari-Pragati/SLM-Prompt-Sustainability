import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])
        self.assertEqual(ntimes_list([0, -1, 0], 3), [0, -3, 0])

    def test_edge_cases(self):
        self.assertEqual(ntimes_list([], 3), [])
        self.assertEqual(ntimes_list([1], 0), [1])
        self.assertEqual(ntimes_list([1], -1), [])

    def test_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_floats(self):
        self.assertListEqual(ntimes_list([1.5, 2.5], 2), [3.0, 5.0])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ntimes_list('abc', 2)
        with self.assertRaises(TypeError):
            ntimes_list([1], 'three')

import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])
        self.assertEqual(ntimes_list([-1, 0, 1], 3), [-3, 0, 3])

    def test_edge_conditions(self):
        self.assertEqual(ntimes_list([], 5), [])
        self.assertEqual(ntimes_list([1], 0), [0])

    def test_boundary_conditions(self):
        self.assertEqual(ntimes_list([1000000000], 1000000000), [1000000000000000000])
        self.assertEqual(ntimes_list([-1000000000], -1000000000), [1000000000000000000])

    def test_complex_cases(self):
        self.assertEqual(ntimes_list([1, 2, 3, 4, 5], -1), [-1, -2, -3, -4, -5])
        self.assertEqual(ntimes_list([1, 2, 3, 4, 5], 0), [0, 0, 0, 0, 0])

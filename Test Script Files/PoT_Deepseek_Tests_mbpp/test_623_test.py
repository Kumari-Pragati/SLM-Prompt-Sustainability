import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])
        self.assertEqual(nth_nums([4, 5, 6], 3), [64, 125, 216])

    def test_edge_cases(self):
        self.assertEqual(nth_nums([0], 1), [0])
        self.assertEqual(nth_nums([0], 0), [1])
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])

    def test_boundary_cases(self):
        self.assertEqual(nth_nums([1000], 1000), [1000**1000])
        self.assertEqual(nth_nums([-1000], 1000), [(-1000)**1000])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            nth_nums("not a list", 2)
        with self.assertRaises(TypeError):
            nth_nums([1, 2, 3], "not an integer")
        with self.assertRaises(ValueError):
            nth_nums([1, 2, 3], -1)

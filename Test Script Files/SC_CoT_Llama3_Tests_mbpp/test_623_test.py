import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 2), [1, 4, 9, 16, 25])

    def test_edge_cases(self):
        self.assertEqual(nth_nums([1], 0), [1])
        self.assertEqual(nth_nums([1], 1), [1])
        self.assertEqual(nth_nums([1, 2, 3], 3), [1, 8, 27])

    def test_boundary_cases(self):
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])
        self.assertEqual(nth_nums([0, 0, 0], 2), [0, 0, 0])

    def test_special_cases(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], -1), [1, 4, 27, 64, 125])
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 3.5), [1, 8, 27, 64, 125])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            nth_nums('a', 2)
        with self.assertRaises(TypeError):
            nth_nums([1, 2, 3], 'a')

import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 2), [1, 4, 9, 16, 25])
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 2), [1, 4, 9, 16, 25])
        self.assertEqual(nth_nums([0, 0, 0, 0, 0], 2), [0, 0, 0, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(nth_nums([1], 0), [1])
        self.assertEqual(nth_nums([1], 1), [1])
        self.assertEqual(nth_nums([], 2), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            nth_nums('abc', 2)
        with self.assertRaises(TypeError):
            nth_nums([1, 2, 3], 'abc')

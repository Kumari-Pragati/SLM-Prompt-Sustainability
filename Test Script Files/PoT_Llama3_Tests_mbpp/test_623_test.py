import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])

    def test_edge_case(self):
        self.assertEqual(nth_nums([1, 2, 3], 0), [1, 1, 1])

    def test_edge_case(self):
        self.assertEqual(nth_nums([1, 2, 3], 1), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(nth_nums([1, 2, 3], 3), [1, 8, 27])

    def test_edge_case(self):
        self.assertEqual(nth_nums([1, 2, 3], -1), [1, 4, 9])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            nth_nums('abc', 2)

import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(removals([10, 10, 10, 10, 10], 5, 3), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5, 6], 6, 2), 1)

    def test_edge_case_1(self):
        self.assertEqual(removals([1, 1, 1, 1, 1], 5, 1), 4)

    def test_edge_case_2(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 4)

    def test_edge_case_3(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 1, 2), 0)

    def test_corner_case_1(self):
        self.assertEqual(removals([], 0, 2), 0)

    def test_corner_case_2(self):
        self.assertEqual(removals([1], 1, 2), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(ValueError):
            removals([1, 2, 3], -1, 2)

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            removals([1, 2, 3], 5, -2)

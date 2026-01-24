import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 3, 5, 7, 9])

    def test_boundary_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), [])

    def test_edge_case(self):
        self.assertEqual(nth_items([], 2), [])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), [])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            nth_items("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", 2)
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "2")

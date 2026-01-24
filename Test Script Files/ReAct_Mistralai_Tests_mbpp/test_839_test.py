import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_ascending(self):
        self.assertListEqual(sort_tuple([(1, 2), (3, 4), (0, 5)]), [(0, 1), (1, 2), (3, 4)])
        self.assertListEqual(sort_tuple([(5, 3), (2, 1), (0, 4)]), [(0, 1), (1, 2), (2, 3), (3, 4)])
        self.assertListEqual(sort_tuple([(100, 200), (300, 400), (0, 5)]), [(0, 1), (1, 2), (300, 400), (100, 200)])

    def test_sort_descending(self):
        self.assertListEqual(sort_tuple([(1, 2), (3, 4), (0, 5)], reverse=True), [(3, 2), (2, 1), (0, 5)])
        self.assertListEqual(sort_tuple([(5, 3), (2, 1), (0, 4)], reverse=True), [(5, 3), (2, 1), (0, 4)])
        self.assertListEqual(sort_tuple([(100, 200), (300, 400), (0, 5)], reverse=True), [(300, 400), (100, 200), (0, 5)])

    def test_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_single_element(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_single_element_reverse(self):
        self.assertEqual(sort_tuple([(1, 2)], reverse=True), [(1, 2)])

    def test_duplicate_elements(self):
        self.assertListEqual(sort_tuple([(1, 2), (1, 3), (1, 4)]), [(1, 2), (1, 3), (1, 4)])

    def test_duplicate_elements_reverse(self):
        self.assertListEqual(sort_tuple([(1, 2), (1, 3), (1, 4)], reverse=True), [(1, 4), (1, 3), (1, 2)])

    def test_mixed_tuples_and_lists(self):
        self.assertListEqual(sort_tuple([(1, 2), [3, 4], (0, 5)]), [(0, 1), (1, 2), [3, 4]])

    def test_mixed_tuples_and_lists_reverse(self):
        self.assertListEqual(sort_tuple([(1, 2), [3, 4], (0, 5)], reverse=True), [([3, 4], 1), (1, 2), (0, 5)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(123)
        with self.assertRaises(TypeError):
            sort_tuple(["a", "b", "c"])
        with self.assertRaises(TypeError):
            sort_tuple([(1, "a"), (2, "b")])

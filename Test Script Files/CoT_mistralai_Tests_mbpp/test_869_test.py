import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_list_range([], 1, 1), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_list_range([(1, 1)], 1, 1), [(1, 1)])
        self.assertListEqual(remove_list_range([(1, 1)], 0, 1), [])
        self.assertListEqual(remove_list_range([(1, 1)], 1, 2), [])

    def test_list_with_single_range(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6)], 1, 3), [(1, 2)])

    def test_list_with_multiple_ranges(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (1, 3)], 1, 3), [(1, 2), (1, 3)])

    def test_list_with_overlapping_ranges(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (2, 5), (1, 3)], 1, 4), [(1, 2), (2, 5)])

    def test_list_with_invalid_input(self):
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], 'a', 'b')
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], 1.5, 2.5)
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], (1, 'a'), (2, 'b'))

import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, specified_element, [], 0)

    def test_single_list(self):
        self.assertEqual(specified_element([(1, 2), (3, 4)], 0), [1])
        self.assertEqual(specified_element([(1, 2), (3, 4)], 1), [2])

    def test_multiple_lists(self):
        self.assertEqual(specified_element([(1, 2), (3, 4), (5, 6)], 0), [1, 3, 5])
        self.assertEqual(specified_element([(1, 2), (3, 4), (5, 6)], 1), [2, 4, 6])

    def test_negative_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2), (3, 4)], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2), (3, 4)], 2)

    def test_lists_with_non_tuples(self):
        self.assertRaises(TypeError, specified_element, [1, 2, 3], 0)

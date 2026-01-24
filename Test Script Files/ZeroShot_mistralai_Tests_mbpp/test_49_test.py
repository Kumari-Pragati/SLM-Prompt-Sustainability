import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(specified_element([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(specified_element([(1, 2)], 0), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(specified_element([(1, 2), (3, 4), (5, 6)], 1), [2, 4, 6])

    def test_negative_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2)], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2)], 2)

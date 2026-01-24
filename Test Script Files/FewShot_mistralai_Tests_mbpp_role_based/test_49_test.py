import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_valid_input(self):
        nums = [(1, 2, 3), (4, 5, 6)]
        self.assertEqual(specified_element(nums, 1), [2, 5])

    def test_empty_list(self):
        self.assertRaises(IndexError, specified_element, [], 0)

    def test_negative_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2, 3)], -1)

    def test_list_with_single_tuple(self):
        self.assertEqual(specified_element([(1, 2, 3)], 1), [2])

    def test_list_with_single_element_tuple(self):
        self.assertEqual(specified_element([(1,)], 0), [1])

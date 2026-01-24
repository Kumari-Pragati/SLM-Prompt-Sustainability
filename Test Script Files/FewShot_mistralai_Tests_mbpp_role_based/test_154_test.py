import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_valid_input(self):
        nums = [(1, 2, 3), (4, 5, 6)]
        self.assertEqual(specified_element(nums, 0), [1, 4])
        self.assertEqual(specified_element(nums, 1), [2, 5])
        self.assertEqual(specified_element(nums, 2), [3, 6])

    def test_empty_list(self):
        self.assertRaises(IndexError, specified_element, [], 0)

    def test_negative_index(self):
        self.assertRaises(IndexError, specified_element, [(1, 2, 3), (4, 5, 6)], -1)

    def test_list_with_single_element(self):
        self.assertEqual(specified_element([(1,)], 0), [1])

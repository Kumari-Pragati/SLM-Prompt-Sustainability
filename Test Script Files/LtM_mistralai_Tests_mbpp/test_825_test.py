import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_simple_input(self):
        nums = [1, 2, 3, 4, 5]
        index = [1, 3]
        self.assertListEqual(access_elements(nums, index), [2, 3])

    def test_empty_input(self):
        nums = []
        index = []
        self.assertListEqual(access_elements(nums, index), [])

    def test_negative_index(self):
        nums = [1, 2, 3, 4, 5]
        index = [-1, 0, 4]
        self.assertListEqual(access_elements(nums, index), [nums[-1], nums[0], nums[4]])

    def test_out_of_range_index(self):
        nums = [1, 2, 3, 4, 5]
        index = [6, -1, -2]
        self.assertListEqual(access_elements(nums, index), [nums[-1], nums[-2], None])

    def test_mixed_input(self):
        nums = [1, 2, 3, 4, 5]
        index = [-1, 0, 4, 6]
        self.assertListEqual(access_elements(nums, index), [nums[-1], nums[0], nums[4], None])

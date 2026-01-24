import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_single_list(self):
        nums = [[1, 2, 2, 3], [2, 2, 3, 3]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1, 2: 4, 3: 4})

    def test_multiple_lists(self):
        nums = [[1, 2, 2, 3], [2, 2, 3, 3], [4, 5, 5, 6]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1, 2: 4, 3: 4, 4: 2, 5: 2, 6: 1})

    def test_empty_list(self):
        nums = []
        result = freq_element(nums)
        self.assertEqual(result, {})

    def test_single_element_list(self):
        nums = [[1, 1, 1, 1]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 4})

    def test_empty_list_of_lists(self):
        nums = []
        result = freq_element(nums)
        self.assertEqual(result, {})

import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
        result = freq_element(nums)
        expected_result = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1})
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        nums = []
        result = freq_element(nums)
        expected_result = Counter()
        self.assertEqual(result, expected_result)

    def test_single_list(self):
        nums = [[1, 2, 3]]
        result = freq_element(nums)
        expected_result = Counter({1: 1, 2: 1, 3: 1})
        self.assertEqual(result, expected_result)

    def test_duplicate_elements(self):
        nums = [[1, 1, 2, 2], [2, 2, 3, 3]]
        result = freq_element(nums)
        expected_result = Counter({1: 2, 2: 4, 3: 2})
        self.assertEqual(result, expected_result)

    def test_empty_sublists(self):
        nums = [[]]
        result = freq_element(nums)
        expected_result = Counter()
        self.assertEqual(result, expected_result)

import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = freq_element(nums)
        expected_result = {1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        nums = []
        result = freq_element(nums)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_single_list(self):
        nums = [[1, 2, 3, 4, 5]]
        result = freq_element(nums)
        expected_result = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        nums = [[1]]
        result = freq_element(nums)
        expected_result = {1: 1}
        self.assertEqual(result, expected_result)

    def test_empty_sublists(self):
        nums = [[]]
        result = freq_element(nums)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            freq_element(None)

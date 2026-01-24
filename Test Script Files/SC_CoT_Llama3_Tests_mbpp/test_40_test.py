import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_typical_input(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1, 2: 2, 3: 2, 4: 2, 5: 1})

    def test_edge_case_empty_input(self):
        nums = []
        result = freq_element(nums)
        self.assertEqual(result, {})

    def test_edge_case_single_list(self):
        nums = [[1, 2, 3]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1, 2: 1, 3: 1})

    def test_edge_case_single_element(self):
        nums = [[1]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1})

    def test_edge_case_empty_list(self):
        nums = [[]]
        result = freq_element(nums)
        self.assertEqual(result, {})

    def test_edge_case_single_empty_list(self):
        nums = [[[]]]
        result = freq_element(nums)
        self.assertEqual(result, {})

    def test_edge_case_multiple_empty_lists(self):
        nums = [[], [], []]
        result = freq_element(nums)
        self.assertEqual(result, {})

    def test_edge_case_multiple_single_elements(self):
        nums = [[1], [2], [3]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 1, 2: 1, 3: 1})

    def test_edge_case_multiple_single_elements_with_duplicates(self):
        nums = [[1, 1], [2, 2], [3, 3]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 2, 3: 2})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list(self):
        nums = [[1, 1], [2, 2], [3, 3], []]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 2, 3: 2})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 2, 3: 2})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list_and_multiple_empty_lists(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]], [[]]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 2, 3: 2})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list_and_multiple_empty_lists_and_single_list(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]], [[]], [[1, 2, 3]]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 1, 3: 1})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list_and_multiple_empty_lists_and_single_list_and_single_empty_list(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]], [[]], [[1, 2, 3]], [[[]]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 1, 3: 1})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list_and_multiple_empty_lists_and_single_list_and_single_empty_list_and_single_list(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]], [[]], [[1, 2, 3]], [[[]]], [[1, 2, 3]]
        result = freq_element(nums)
        self.assertEqual(result, {1: 2, 2: 1, 3: 1})

    def test_edge_case_multiple_single_elements_with_duplicates_and_empty_list_and_single_empty_list_and_multiple_empty_lists_and_single_list_and_single_empty_list_and_single_list_and_single_empty_list(self):
        nums = [[1, 1], [2, 2], [3, 3], [], [[]], [[]], [[1, 2, 3]], [[[]]], [[1, 2, 3]], [[[]]]
        result =
import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_empty_list(self):
        result = frequency_lists([])
        self.assertDictEqual(result, {})

    def test_single_element_list(self):
        result = frequency_lists([[1]])
        self.assertDictEqual(result, {'1': 1})

    def test_single_element_list_multiple_occurrences(self):
        result = frequency_lists([[1, 1]])
        self.assertDictEqual(result, {'1': 2})

    def test_multiple_elements_list(self):
        result = frequency_lists([[1, 2, 3], [2, 3, 4], [1, 2, 3]])
        self.assertDictEqual(result, {'1': 3, '2': 2, '3': 3, '4': 1})

    def test_duplicate_sublists(self):
        result = frequency_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertDictEqual(result, {'1': 3, '2': 3, '3': 3})

    def test_negative_numbers(self):
        result = frequency_lists([[-1, -2, -3], [2, -1, 0], [-1, 1, -1]])
        self.assertDictEqual(result, {'-1': 3, '0': 1, '1': 1, '2': 1, '-3': 1})

    def test_zero(self):
        result = frequency_lists([[0], [1, 0], [0, 0]])
        self.assertDictEqual(result, {'0': 3, '1': 1})

    def test_large_numbers(self):
        result = frequency_lists([[1000000, 2000000, 3000000], [2000000, 3000000, 4000000], [1000000, 2000000, 3000000]])
        self.assertDictEqual(result, {'1000000': 3, '2000000': 3, '3000000': 3, '4000000': 1})

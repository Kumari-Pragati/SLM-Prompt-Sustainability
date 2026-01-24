import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_simple_list(self):
        self.assertDictEqual(frequency_lists([[1, 1], [2, 2], [1, 1]]), {'1': 3, '2': 2})

    def test_empty_list(self):
        self.assertDictEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(frequency_lists([[1]]), {'1': 1})

    def test_negative_numbers(self):
        self.assertDictEqual(frequency_lists([[-1, -1], [2, 2], [-1, -1]]), {'-1': 2, '2': 2})

    def test_large_numbers(self):
        self.assertDictEqual(frequency_lists([[1000000, 1000000], [2, 2], [1000000, 1000000]]), {'1000000': 2, '2': 2})

    def test_mixed_types(self):
        self.assertDictEqual(frequency_lists([[1, 'a'], [2, 2], [1, 'a']]), {'1': 2, '2': 2})

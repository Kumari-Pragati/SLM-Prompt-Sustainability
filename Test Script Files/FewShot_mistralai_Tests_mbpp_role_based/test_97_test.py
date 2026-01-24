import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(frequency_lists([[1]]), {1: 1})

    def test_single_element_list_multiple_occurrences(self):
        self.assertDictEqual(frequency_lists([[1, 1]]), {1: 2})

    def test_multiple_elements_list(self):
        self.assertDictEqual(frequency_lists([[1, 2, 3], [3, 2, 1]]), {1: 2, 2: 2, 3: 2})

    def test_negative_numbers(self):
        self.assertDictEqual(frequency_lists([[-1, -2, -3], [-3, -2, -1]]), {-1: 2, -2: 2, -3: 2})

    def test_duplicate_sublists(self):
        self.assertDictEqual(frequency_lists([[1, 2, 3], [1, 2, 3]]), {1: 2, 2: 2, 3: 2})

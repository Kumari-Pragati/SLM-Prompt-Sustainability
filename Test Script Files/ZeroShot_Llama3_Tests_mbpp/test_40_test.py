import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_freq_element(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {1: 1, 2: 2, 3: 2, 4: 2, 5: 1})

    def test_freq_element_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_freq_element_single_list(self):
        self.assertEqual(freq_element([[1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_freq_element_multiple_lists(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]), {1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1})

    def test_freq_element_duplicates(self):
        self.assertEqual(freq_element([[1, 2, 2, 3, 3, 3]]), {1: 1, 2: 2, 3: 3})

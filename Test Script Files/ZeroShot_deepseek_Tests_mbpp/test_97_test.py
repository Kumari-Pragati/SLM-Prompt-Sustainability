import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_single_list(self):
        self.assertEqual(frequency_lists([1, 2, 3, 4, 5]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1})

    def test_nested_list(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [3, 4, 5], [5, 6, 7]]), {1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 1, 7: 1})

    def test_mixed_list(self):
        self.assertEqual(frequency_lists([[1, 2, 'a'], [3, 'b', 4], [5, 'c', 6]]), {1: 1, 2: 1, 'a': 1, 3: 1, 'b': 1, 4: 1, 5: 1, 'c': 1, 6: 1})

    def test_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

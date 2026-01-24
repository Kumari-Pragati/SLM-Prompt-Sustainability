import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4]]), {1: 1, 2: 2, 3: 2, 4: 1})

    def test_duplicates_in_list(self):
        self.assertEqual(frequency_lists([[1, 2, 2, 3, 3, 3]]), {1: 1, 2: 2, 3: 3})

    def test_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, 2, -2, 3]]), {-1: 1, 2: 1, -2: 1, 3: 1})

    def test_non_integer_values(self):
        self.assertEqual(frequency_lists([['a', 'b', 'c'], ['a', 'c', 'd']]), {'a': 2, 'b': 1, 'c': 2, 'd': 1})

import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4]]), {1: 1, 2: 2, 3: 2, 4: 1})

    def test_empty_input(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_element_input(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_duplicate_elements(self):
        self.assertEqual(frequency_lists([[1, 1, 2, 2], [2, 2, 3, 3]]), {1: 2, 2: 4, 3: 4})

    def test_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, -2, -2], [-2, -2, -3]]), {-1: 1, -2: 3, -3: 1})

    def test_mixed_numbers(self):
        self.assertEqual(frequency_lists([[1, -1, 2, -2], [-1, -2, 2, 2]]), {1: 1, -1: 2, -2: 2, 2: 2})

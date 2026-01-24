import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [4, 5, 6]]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})

    def test_duplicates_in_list(self):
        self.assertEqual(frequency_lists([[1, 1, 2, 2, 3, 3]]), {1: 2, 2: 2, 3: 2})

    def test_empty_sublist(self):
        self.assertEqual(frequency_lists([[], [1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, -2, -3]]), {-1: 1, -2: 1, -3: 1})

    def test_zero(self):
        self.assertEqual(frequency_lists([[0, 1, 2]]), {0: 1, 1: 1, 2: 1})

    def test_max_value(self):
        self.assertEqual(frequency_lists([[100, 200, 300]]), {100: 1, 200: 1, 300: 1})

    def test_min_value(self):
        self.assertEqual(frequency_lists([[-100, -200, -300]]), {-100: 1, -200: 1, -300: 1})

import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), collections.Counter({1: 1}))

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), collections.Counter({1: 1, 2: 2, 3: 3}))

    def test_list_with_duplicates(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 3, 3, 3]), collections.Counter({1: 2, 2: 2, 3: 3}))

    def test_list_with_negative_numbers(self):
        self.assertEqual(freq_count([-1, -1, 0, 0, 1, 1]), collections.Counter({-1: 2, 0: 2, 1: 2}))

    def test_list_with_non_integer_values(self):
        self.assertEqual(freq_count([1, 2.0, 2.0, 3, 3, 3]), collections.Counter({1: 1, 2.0: 2, 3: 3}))

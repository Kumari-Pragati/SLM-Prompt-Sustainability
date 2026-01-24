import unittest
from mbpp_40_code import Counter
from itertools import chain
from 40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(freq_element([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 3]), Counter({1: 2, 2: 2, 3: 1}))

    def test_empty_list(self):
        self.assertEqual(freq_element([]), Counter())

    def test_list_with_duplicates_and_non_numbers(self):
        self.assertRaises(TypeError, freq_element, [1, 'a', 2, 'b', 3])

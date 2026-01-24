import unittest
from mbpp_686_code import defaultdict
from six.moves import range
from six.moves import zip_longest

from 686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), "{}")

    def test_single_element(self):
        self.assertEqual(freq_element([1]), "{'1': 1}")

    def test_multiple_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 3, 3]), "{'1': 2, '2': 2, '3': 2}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 2, 3, 3, 3]), "{'1': 2, '2': 3, '3': 3}")

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, freq_element, [1, "a", 2.5])

    def test_long_list(self):
        long_list = [1] + [0] * 1000000
        self.assertEqual(freq_element(long_list), "{'0': 1000000, '1': 1}")

    def test_large_numbers(self):
        large_numbers = list(range(1000000))
        self.assertEqual(freq_element(large_numbers), "{'0': 999999, '1': 1, '2': 1, ..., '999998': 1}")

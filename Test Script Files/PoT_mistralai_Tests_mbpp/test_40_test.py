import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(freq_element([1, 2, 2, 3, 3, 3, 4, 4, 4]), {'1': 1, '2': 2, '3': 3, '4': 4})

    def test_empty_list(self):
        self.assertDictEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(freq_element([1]), {'1': 1})

    def test_negative_numbers(self):
        self.assertDictEqual(freq_element([-1, -2, -2, -3, -3, -3, -4, -4, -4]), {'-1': 1, '-2': 2, '-3': 3, '-4': 4})

    def test_duplicate_zero(self):
        self.assertDictEqual(freq_element([0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4]), {'0': 2, '1': 1, '2': 2, '3': 3, '4': 4})

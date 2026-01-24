import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(freq_element([1]), {'1': 1})

    def test_multiple_elements(self):
        self.assertDictEqual(freq_element([1, 2, 1, 3, 2, 1]), {'1': 3, '2': 2, '3': 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(freq_element([1, 1, 2, 2, 3, 3, 3]), {'1': 2, '2': 2, '3': 3})

    def test_negative_numbers(self):
        self.assertDictEqual(freq_element([-1, -2, -1, 3, -2, -1]), {'-1': 3, '-2': 2, '3': 1})

    def test_floats(self):
        self.assertDictEqual(freq_element([1.1, 2.2, 1.1, 3.3, 2.2, 1.1]), {'1.1': 3, '2.2': 2, '3.3': 1})

    def test_mixed_types(self):
        self.assertRaises(TypeError, freq_element, [1, 'a', 2, None])

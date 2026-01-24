import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(count_element_freq([]), {})

    def test_single_element(self):
        self.assertDictEqual(count_element_freq([1]), {'1': 1})

    def test_multiple_elements(self):
        self.assertDictEqual(count_element_freq([1, 1, 2, 2, 3, 3]), {'1': 2, '2': 2, '3': 2})

    def test_mixed_types(self):
        self.assertDictEqual(count_element_freq([1, 'a', (1, 2), [1, 2, 3]]), {'1': 2, 'a': 1, (1, 2): 1, [1, 2, 3]: 1})

    def test_nested_tuples(self):
        self.assertDictEqual(count_element_freq(((1, 2), (1, 2), (3, 4))), {(1, 2): 2, (3, 4): 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(count_element_freq([1, 1, 2, 2, 1, 2]), {'1': 3, '2': 3})

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_element_freq, 'string')

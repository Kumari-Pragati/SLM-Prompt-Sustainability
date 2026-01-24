import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(count_element_freq([]), {})

    def test_single_element(self):
        self.assertDictEqual(count_element_freq([1]), {'1': 1})

    def test_multiple_elements(self):
        self.assertDictEqual(count_element_freq([1, 2, 1, 3, 2, 2]), {'1': 2, '2': 3, '3': 1})

    def test_mixed_types(self):
        self.assertDictEqual(count_element_freq([1, 'a', 1, 'a', 2]), {'1': 2, 'a': 2, '2': 1})

    def test_nested_tuples(self):
        self.assertDictEqual(count_element_freq(((1, 2), (1, 2), 3)), {'1': 2, '2': 2, '3': 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(count_element_freq([1, 1, 2, 2, 3, 3, 3]), {'1': 2, '2': 2, '3': 3})

    def test_large_input(self):
        large_input = [i for i in range(100)]
        self.assertDictEqual(count_element_freq(large_input), {str(i): len(large_input) // 100 for i in range(100)})

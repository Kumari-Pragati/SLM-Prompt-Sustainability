import unittest
from mbpp_88_code import Counter
from your_module import freq_count  # replace 'your_module' with the actual module name

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(freq_count(['a']), {'a': 1})

    def test_duplicate_elements_list(self):
        self.assertDictEqual(freq_count(['a', 'a', 'b', 'b', 'c']), {'a': 2, 'b': 2, 'c': 1})

    def test_list_with_special_characters(self):
        self.assertDictEqual(freq_count(['a', '!', 'b', ' ', 'c', '.', 'd']), {'a': 1, '!': 1, 'b': 1, ' ': 1, 'c': 1, '.': 1, 'd': 1})

    def test_list_with_numbers(self):
        self.assertDictEqual(freq_count(['a', 1, 'b', 2, 'c']), {'a': 1, '1': 1, 'b': 1, '2': 1, 'c': 1})

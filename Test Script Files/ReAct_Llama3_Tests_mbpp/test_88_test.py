import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_duplicates(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2, 3, 3, 3, 3]), {1: 2, 2: 3, 3: 4})

    def test_non_integer_values(self):
        self.assertEqual(freq_count(['a', 'b', 'b', 'c', 'c', 'c']), {'a': 1, 'b': 2, 'c': 3})

    def test_mixed_types(self):
        self.assertEqual(freq_count([1, 'a', 'b', 'b', 2, 2, 3, 3, 3]), {1: 1, 'a': 1, 'b': 2, 2: 2, 3: 3})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            freq_count('not a list')

import unittest
from mbpp_237_code import Counter
from 237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertDictEqual(check_occurences([(1, 2), (1, 2), (3, 4), (1, 2)]), {'(1, 2)': 3, ('3, 4'): 1})

    def test_empty_list(self):
        self.assertDictEqual(check_occurences([]), {})

    def test_single_element(self):
        self.assertDictEqual(check_occurences([(1, 2)]), {'(1, 2)': 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(check_occurences([(1, 2), (1, 2), (1, 2)]), {'(1, 2)': 3})

    def test_unsorted_elements(self):
        self.assertDictEqual(check_occurences([(2, 1), (1, 2)]), {'(1, 2)': 1})

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            check_occurences([(1, 2), 'abc', (3, 4)])

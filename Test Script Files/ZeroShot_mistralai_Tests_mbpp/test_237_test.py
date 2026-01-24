import unittest
from mbpp_237_code import Counter
from 237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(check_occurences([]), {})

    def test_single_element(self):
        self.assertDictEqual(check_occurences([[1, 2]]), {'(1, 2)': 1})

    def test_multiple_elements(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 3], [3, 1]]),
                             {'(1, 2)': 2, '(1, 3)': 2, '(3, 1)': 1})

    def test_duplicates(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 2]]),
                             {'(1, 2)': 2})

    def test_mixed_data_types(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 'a'], [1, 'a']]),
                             {'(1, 2)': 1, '(2, "a")': 1, '(1, "a")': 1})

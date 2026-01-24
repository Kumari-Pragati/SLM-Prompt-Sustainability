import unittest
from mbpp_237_code import Counter
from 237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(check_occurences([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(check_occurences([[1, 2]]), {'(1, 2)': 1})

    def test_multiple_elements_list(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 3]]), {'(1, 2)': 2, '(1, 3)': 1})

    def test_duplicate_elements_list(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 2], [2, 1]]), {'(1, 2)': 3})

    def test_mixed_types_list(self):
        with self.assertRaises(TypeError):
            check_occurences([[1, 2], 'abc', 3])

    def test_unsorted_elements_list(self):
        with self.assertRaises(ValueError):
            check_occurences([[2, 1], [1, 2]])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            check_occurences(123)

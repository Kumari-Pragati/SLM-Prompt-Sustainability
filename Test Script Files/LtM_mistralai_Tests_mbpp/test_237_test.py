import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_simple_list(self):
        self.assertDictEqual(check_occurences([(1, 2), (2, 3), (1, 2)]), {'(1, 2)': 2, ('1, 2': 1, ('2, 3': 1)})

    def test_empty_list(self):
        self.assertDictEqual(check_occurences([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(check_occurences([(1, 2)]), {'(1, 2)': 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(check_occurences([(1, 2), (1, 2)]), {'(1, 2)': 2})

    def test_unsorted_list(self):
        self.assertDictEqual(check_occurences([(2, 1), (1, 2)]), {'(1, 2)': 1, ('2, 1': 1)})

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            check_occurences([(1, 2), (1, '2')])

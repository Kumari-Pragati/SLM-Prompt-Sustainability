import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(check_occurences([]), {})

    def test_single_element_list(self):
        self.assertEqual(check_occurences([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(check_occurences([1, 2, 3, 1, 2, 3]), {1: 2, 2: 2, 3: 2})

    def test_list_with_duplicates(self):
        self.assertEqual(check_occurences([1, 1, 2, 2, 3, 3]), {1: 2, 2: 2, 3: 2})

    def test_list_with_negative_numbers(self):
        self.assertEqual(check_occurences([-1, -2, -3, -1, -2, -3]), {-1: 2, -2: 2, -3: 2})

    def test_list_with_non_integer_numbers(self):
        self.assertEqual(check_occurences([1.0, 2.0, 3.0, 1.0, 2.0, 3.0]), {1.0: 2, 2.0: 2, 3.0: 2})

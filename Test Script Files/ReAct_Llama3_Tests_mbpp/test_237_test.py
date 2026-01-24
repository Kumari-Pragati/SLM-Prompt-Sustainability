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
        self.assertEqual(check_occurences([1, 1, 2, 2, 2, 3, 3, 3, 3]), {1: 2, 2: 3, 3: 4})

    def test_list_with_negative_numbers(self):
        self.assertEqual(check_occurences([-1, -2, -3, -1, -2, -3]), {-1: 2, -2: 2, -3: 2})

    def test_list_with_mixed_types(self):
        self.assertEqual(check_occurences([1, 'a', 2, 'b', 3, 'c']), {(1,): 1, ('a',): 1, (2,): 1, ('b',): 1, (3,): 1, ('c',): 1})

    def test_list_with_empty_elements(self):
        self.assertEqual(check_occurences([1, '', 2, '', 3, '']), {1: 1, '': 3})

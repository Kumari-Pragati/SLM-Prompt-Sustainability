import unittest
from mbpp_893_code import Extract

class TestExtractFunction(unittest.TestCase):

    def test_typical_input(self):
        lst = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        self.assertEqual(Extract(lst), ['c', 'f', 'i'])

    def test_empty_list(self):
        lst = []
        self.assertEqual(Extract(lst), [])

    def test_single_element_list(self):
        lst = [['hello']]
        self.assertEqual(Extract(lst), ['hello'])

    def test_list_of_empty_lists(self):
        lst = [[]]
        self.assertEqual(Extract(lst), [])

    def test_list_of_lists_with_one_element(self):
        lst = [[1], [2], [3]]
        self.assertEqual(Extract(lst), [1, 2, 3])

    def test_list_of_lists_with_multiple_elements(self):
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(Extract(lst), [3, 6, 9])

    def test_list_of_lists_with_empty_and_non_empty_elements(self):
        lst = [[], [1, 2, 3], [4, 5, 6]]
        self.assertEqual(Extract(lst), [3])

    def test_list_of_lists_with_non_empty_and_empty_elements(self):
        lst = [[1, 2, 3], [], [4, 5, 6]]
        self.assertEqual(Extract(lst), [3])

    def test_list_of_lists_with_empty_elements_and_non_empty_elements(self):
        lst = [[], [1, 2, 3], [4, 5, 6]]
        self.assertEqual(Extract(lst), [3])

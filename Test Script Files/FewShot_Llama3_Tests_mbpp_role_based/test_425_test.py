import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 'a'), 0)

    def test_list_with_element(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'a'), 1)

    def test_list_without_element(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'd'), 0)

    def test_list_with_multiple_elements(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'a'], 'a'), 2)

    def test_list_with_sublist(self):
        self.assertEqual(count_element_in_list([['a', 'b'], ['c', 'd']], 'a'), 1)

    def test_list_with_sublist_and_element(self):
        self.assertEqual(count_element_in_list([['a', 'b'], ['c', 'd']], 'b'), 1)

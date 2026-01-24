import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 'a'), 0)

    def test_list_without_element(self):
        self.assertEqual(count_element_in_list(['b', 'c', 'd'], 'e'), 0)

    def test_list_with_element(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'a'), 1)

    def test_list_with_multiple_elements(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'a'], 'a'), 2)

    def test_list_with_element_at_end(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'd'], 'd'), 1)

    def test_list_with_element_at_start(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'd'], 'a'), 1)

    def test_list_with_element_in_middle(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'd'], 'b'), 1)

    def test_list_with_element_at_multiple_positions(self):
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'a'], 'a'), 2)

    def test_list_with_element_at_all_positions(self):
        self.assertEqual(count_element_in_list(['a', 'a', 'a', 'a'], 'a',), 4)

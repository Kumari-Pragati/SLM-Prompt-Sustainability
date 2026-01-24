import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_empty_list_and_array(self):
        self.assertListEqual(most_common_elem('', 1), [])
        self.assertListEqual(most_common_elem([], 1), [])

    def test_single_element_list_and_array(self):
        self.assertListEqual(most_common_elem('a', 1), [('a', 1)])
        self.assertListEqual(most_common_elem([1], 1), [(1, 1)])

    def test_multiple_elements_list_and_array(self):
        self.assertListEqual(most_common_elem('aaabbc', 2), [('a', 3), ('b', 2)])
        self.assertListEqual(most_common_elem([1, 2, 1, 3, 2, 1], 2), [(1, 3), (2, 2)])

    def test_single_element_in_longer_list_and_array(self):
        self.assertListEqual(most_common_elem('aaabbcde', 1), [('a', 1)])
        self.assertListEqual(most_common_elem([1, 2, 3, 4, 5], 1), [(1, 1)])

    def test_different_lengths(self):
        self.assertListEqual(most_common_elem('aaabbc', 2), [('a', 3), ('b', 2)])
        self.assertRaises(ValueError, most_common_elem, 'aaabbc', 3)

        self.assertListEqual(most_common_elem([1, 2, 1, 3, 2, 1], 2), [(1, 3), (2, 2)])
        self.assertRaises(ValueError, most_common_elem, [1, 2, 1, 3, 2, 1], 3)

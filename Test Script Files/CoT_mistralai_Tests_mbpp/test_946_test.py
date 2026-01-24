import unittest
from mbpp_946_code import Counter
from nine_hundred_forty_six_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_empty_list_and_zero_count(self):
        self.assertListEqual(most_common_elem('', 0), [])

    def test_single_element_list(self):
        self.assertListEqual(most_common_elem(['a']), [('a', 1)])

    def test_multiple_elements_list(self):
        self.assertListEqual(most_common_elem(['a', 'b', 'a', 'c', 'a', 'b']), [('a', 4), ('b', 2)])

    def test_list_with_duplicates_and_single_count(self):
        self.assertListEqual(most_common_elem(['a', 'b', 'a', 'a', 'b', 'a']), [('a', 3), ('b', 2)])

    def test_list_with_duplicates_and_multiple_count(self):
        self.assertListEqual(most_common_elem(['a', 'b', 'a', 'a', 'b', 'a'], 2), [('a', 3), ('b', 2)])

    def test_list_with_only_one_element(self):
        self.assertListEqual(most_common_elem(['a']), [('a', 1)])

    def test_list_with_multiple_elements_and_zero_count(self):
        self.assertListEqual(most_common_elem(['a', 'b', 'c'], 0), [])

    def test_list_with_empty_string(self):
        self.assertListEqual(most_common_elem('', 1), [('', 1)])

    def test_list_with_only_spaces(self):
        self.assertListEqual(most_common_elem(['   '], 1), [(' ', 1)])

    def test_list_with_invalid_input(self):
        self.assertRaises(TypeError, most_common_elem, 123, 4)
        self.assertRaises(TypeError, most_common_elem, 'abc', 1.5)

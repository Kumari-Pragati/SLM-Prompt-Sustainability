import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 1), 0)

    def test_single_element_list(self):
        self.assertEqual(count_element_in_list([1], 1), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 1, 2, 3], 1), 3)
        self.assertEqual(count_element_in_list([1, 2, 3, 1, 2, 3], 2), 2)
        self.assertEqual(count_element_in_list([1, 2, 3, 1, 2, 3], 3), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(count_element_in_list([1, 1, 2, 2, 3, 3, 1, 1], 1), 4)

    def test_list_with_non_existent_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3], 4), 0)

    def test_list_with_none_type_element(self):
        self.assertRaises(TypeError, count_element_in_list, [1, 2, 3], None)

    def test_list_with_string_element(self):
        self.assertRaises(TypeError, count_element_in_list, [1, 'two', 3], 1)

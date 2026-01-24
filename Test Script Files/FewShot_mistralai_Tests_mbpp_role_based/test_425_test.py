import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_count_single_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)

    def test_count_multiple_elements(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5, 3, 3], 3), 3)

    def test_count_empty_list(self):
        self.assertEqual(count_element_in_list([], 3), 0)

    def test_count_non_existent_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 6), 0)

    def test_count_list_with_none(self):
        self.assertEqual(count_element_in_list([None, 2, 3, 4, 5], None), 1)

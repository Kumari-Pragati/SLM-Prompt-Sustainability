import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 42), 0)

    def test_single_element(self):
        self.assertEqual(count_element_in_list([42], 42), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 42, 42, 42, 5, 6], 42), 4)

    def test_non_existent_element(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4], 42), 0)

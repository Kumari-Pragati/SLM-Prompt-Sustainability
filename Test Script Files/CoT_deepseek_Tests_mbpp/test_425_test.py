import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5), 1)

    def test_element_not_in_list(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10), 0)

    def test_empty_list(self):
        self.assertEqual(count_element_in_list([], 1), 0)

    def test_element_in_sublist(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 1)

    def test_element_in_multiple_sublists(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9, 5]], 5), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_element_in_list("not a list", 1)

    def test_invalid_sublist_type(self):
        with self.assertRaises(TypeError):
            count_element_in_list([1, 2, 3], 1)

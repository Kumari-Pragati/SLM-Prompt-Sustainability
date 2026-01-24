import unittest

from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_typical_case(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_empty_list(self):
        lists = []
        expected_output = []
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_single_list(self):
        lists = [[1, 2, 3]]
        expected_output = [[3, 2, 1]]
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_duplicate_elements(self):
        lists = [[1, 2, 2], [3, 3, 3], [4, 4, 4]]
        expected_output = [[2, 2, 1], [3, 3, 3], [4, 4, 4]]
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_negative_numbers(self):
        lists = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_output = [[-3, -2, -1], [-6, -5, -4], [-9, -8, -7]]
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_single_element_lists(self):
        lists = [[1], [2], [3]]
        expected_output = [[1], [2], [3]]
        self.assertEqual(reverse_list_lists(lists), expected_output)

    def test_invalid_input(self):
        lists = [1, 2, 3]
        with self.assertRaises(TypeError):
            reverse_list_lists(lists)

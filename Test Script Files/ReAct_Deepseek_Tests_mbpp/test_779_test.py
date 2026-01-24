import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_typical_case(self):
        input_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
        expected_output = {(1, 2, 3): 2, (4, 5, 6): 1}
        self.assertEqual(unique_sublists(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = {}
        self.assertEqual(unique_sublists(input_list), expected_output)

    def test_single_sublist(self):
        input_list = [[1, 2, 3]]
        expected_output = {(1, 2, 3): 1}
        self.assertEqual(unique_sublists(input_list), expected_output)

    def test_duplicate_sublists(self):
        input_list = [[1, 2, 3], [1, 2, 3]]
        expected_output = {(1, 2, 3): 2}
        self.assertEqual(unique_sublists(input_list), expected_output)

    def test_sublists_with_duplicates(self):
        input_list = [[1, 2, 3], [3, 2, 1]]
        expected_output = {(1, 2, 3): 1, (3, 2, 1): 1}
        self.assertEqual(unique_sublists(input_list), expected_output)

    def test_sublists_with_same_elements(self):
        input_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected_output = {(1, 2, 3): 3}
        self.assertEqual(unique_sublists(input_list), expected_output)

import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):
    def test_single_group(self):
        input_data = [('a', 'b', 'c')]
        expected_output = [('a', 'b', 'c')]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_multiple_groups(self):
        input_data = [('a', 'b', 'c'), ('a', 'd', 'e'), ('f', 'g', 'h')]
        expected_output = [('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h')]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_empty_input(self):
        input_data = []
        expected_output = []
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_single_element_group(self):
        input_data = [('a',)]
        expected_output = [('a',)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_group_with_duplicates(self):
        input_data = [('a', 'a', 'b', 'c'), ('a', 'd', 'e'), ('f', 'g', 'h')]
        expected_output = [('a', 'a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h')]
        self.assertEqual(group_tuples(input_data), expected_output)

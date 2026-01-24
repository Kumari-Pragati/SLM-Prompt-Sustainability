import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(list_split('hello', 2), ['he', 'll', 'o'])

    def test_edge_case_step_one(self):
        self.assertEqual(list_split('hello', 1), ['h', 'e', 'l', 'l', 'o'])

    def test_edge_case_step_zero(self):
        with self.assertRaises(ValueError):
        list_split('hello', 0)

    def test_edge_case_step_negative(self):
        with self.assertRaises(ValueError):
        list_split('hello', -1)

    def test_edge_case_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_edge_case_single_character(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_edge_case_single_character_step_one(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_edge_case_single_character_step_two(self):
        self.assertEqual(list_split('a', 2), [])

    def test_edge_case_single_character_step_zero(self):
        with self.assertRaises(ValueError):
        list_split('a', 0)

    def test_edge_case_single_character_step_negative(self):
        with self.assertRaises(ValueError):
        list_split('a', -1)

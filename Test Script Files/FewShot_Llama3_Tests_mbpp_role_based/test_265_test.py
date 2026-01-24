import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(list_split('abcdefgh', 2), ['ab', 'cd', 'ef', 'gh'])

    def test_edge_case_step_one(self):
        self.assertEqual(list_split('abcdefgh', 1), ['abcdefgh'])

    def test_edge_case_step_zero(self):
        with self.assertRaises(ValueError):
            list_split('abcdefgh', 0)

    def test_edge_case_step_negative(self):
        with self.assertRaises(ValueError):
            list_split('abcdefgh', -1)

    def test_edge_case_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_edge_case_single_character(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_edge_case_single_character_step_two(self):
        self.assertEqual(list_split('a', 2), [])

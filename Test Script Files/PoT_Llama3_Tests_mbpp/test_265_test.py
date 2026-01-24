import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(list_split('abcdef', 2), ['ab', 'cd', 'ef'])

    def test_edge_case_step_one(self):
        self.assertEqual(list_split('abcdef', 1), ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_edge_case_step_string(self):
        with self.assertRaises(TypeError):
            list_split('abcdef', 'two')

    def test_edge_case_step_zero(self):
        with self.assertRaises(ZeroDivisionError):
            list_split('abcdef', 0)

    def test_edge_case_step_negative(self):
        with self.assertRaises(ValueError):
            list_split('abcdef', -2)

    def test_edge_case_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_edge_case_single_character(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_edge_case_single_character_step_one(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_edge_case_single_character_step_two(self):
        self.assertEqual(list_split('a', 2), ['a'])

    def test_edge_case_single_character_step_three(self):
        self.assertEqual(list_split('a', 3), ['a'])

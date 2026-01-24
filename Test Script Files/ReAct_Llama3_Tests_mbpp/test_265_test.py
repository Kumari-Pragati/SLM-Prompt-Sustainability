import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(list_split('HelloWorld', 2), ['He', 'llo', 'Wo', 'rld'])

    def test_edge_case_step_1(self):
        self.assertEqual(list_split('HelloWorld', 1), ['HelloWorld'])

    def test_edge_case_step_length(self):
        self.assertEqual(list_split('HelloWorld', len('HelloWorld')), ['HelloWorld'])

    def test_edge_case_step_zero(self):
        with self.assertRaises(ValueError):
            list_split('HelloWorld', 0)

    def test_edge_case_step_negative(self):
        with self.assertRaises(ValueError):
            list_split('HelloWorld', -1)

    def test_edge_case_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_edge_case_single_character(self):
        self.assertEqual(list_split('a', 1), ['a'])

import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(list_split('HelloWorld', 2), ['He', 'llo', 'Wo', 'rld'])

    def test_edge_cases(self):
        self.assertEqual(list_split('HelloWorld', 1), ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'])
        self.assertEqual(list_split('HelloWorld', 3), ['Hel', 'loW', 'rld'])

    def test_step_zero(self):
        with self.assertRaises(ValueError):
            list_split('HelloWorld', 0)

    def test_step_negative(self):
        with self.assertRaises(ValueError):
            list_split('HelloWorld', -1)

    def test_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_single_character_string(self):
        self.assertEqual(list_split('a', 1), ['a'])

    def test_step_one(self):
        self.assertEqual(list_split('HelloWorld', 1), ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'])

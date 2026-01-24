import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(char_frequency('aabbc'), {'a': 2, 'b': 2, 'c': 1})
        self.assertEqual(char_frequency('122333'), {'1': 1, '2': 2, '3': 3})

    def test_edge_conditions(self):
        self.assertEqual(char_frequency(''), {})
        self.assertEqual(char_frequency('a'), {'a': 1})

    def test_complex_cases(self):
        self.assertEqual(char_frequency('abcdefg'), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})
        self.assertEqual(char_frequency('aaaabbbbb'), {'a': 4, 'b': 5})

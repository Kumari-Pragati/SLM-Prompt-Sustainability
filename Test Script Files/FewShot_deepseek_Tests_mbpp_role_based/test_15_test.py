import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(split_lowerstring('HelloWorld'), ['ello', 'orld'])

    def test_edge_condition(self):
        self.assertEqual(split_lowerstring(''), [])

    def test_boundary_condition(self):
        self.assertEqual(split_lowerstring('a'), ['a'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_lowerstring(123)

    def test_mixed_case_string(self):
        self.assertEqual(split_lowerstring('HelloWORLD'), ['ello', 'orld'])

    def test_string_with_numbers(self):
        self.assertEqual(split_lowerstring('Hello123World456'), ['ello', 'orld'])

    def test_string_with_special_characters(self):
        self.assertEqual(split_lowerstring('Hello@#$World'), ['ello', 'orld'])

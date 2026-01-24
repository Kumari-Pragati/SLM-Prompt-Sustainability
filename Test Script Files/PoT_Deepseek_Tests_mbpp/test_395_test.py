import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')
        self.assertEqual(first_non_repeating_character('abcabc'), None)
        self.assertEqual(first_non_repeating_character('aabbcc'), None)
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_edge_cases(self):
        self.assertEqual(first_non_repeating_character(''), None)
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_corner_cases(self):
        self.assertEqual(first_non_repeating_character('aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz'), None)
        self.assertEqual(first_non_repeating_character('aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz'), 'z')

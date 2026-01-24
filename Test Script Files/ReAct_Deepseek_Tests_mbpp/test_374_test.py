import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertIn('ab', permute_string('ab'))
        self.assertIn('ba', permute_string('ab'))

    def test_three_character_string(self):
        permutations = permute_string('abc')
        self.assertIn('abc', permutations)
        self.assertIn('acb', permutations)
        self.assertIn('bac', permutations)
        self.assertIn('bca', permutations)
        self.assertIn('cab', permutations)
        self.assertIn('cba', permutations)

    def test_duplicate_characters(self):
        self.assertIn('aab', permute_string('aba'))
        self.assertIn('aba', permute_string('aba'))
        self.assertIn('baa', permute_string('aba'))

    def test_large_string(self):
        # This test may take a while to run, but it's important to ensure
        # that the function can handle large inputs.
        permutations = permute_string('abcdef')
        self.assertEqual(len(permutations), 720)  # 6!

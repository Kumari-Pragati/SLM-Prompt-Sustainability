import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(permute_string('ab'), ['a', 'ba'])

    def test_multiple_characters_string(self):
        self.assertEqual(permute_string('abc'), ['a', 'ac', 'bc', 'ab', 'acb', 'bac', 'bca'])

    def test_long_string(self):
        self.assertEqual(permute_string('xyzabcdefg'), [
            'x', 'y', 'z', 'xy', 'xz', 'yx', 'yz', 'wxy', 'wzx', 'wyx', 'wzy',
            'abc', 'acb', 'bac', 'ab', 'ac', 'bc', 'abd', 'acd', 'bacd', 'bcd', 'abcd',
            'abce', 'acde', 'bace', 'bade', 'bcde', 'abcf', 'acf', 'bcf', 'abcg', 'acg', 'bacg', 'bag', 'bcg',
            'abch', 'ach', 'bch', 'abci', 'achi', 'bci', 'abcg', 'acgh', 'bacg', 'bagh', 'bcgh',
            'abchi', 'achi', 'bchi', 'abch', 'ach', 'bch', 'abci', 'achi', 'bci'
        ])

    def test_duplicate_characters(self):
        self.assertEqual(permute_string('aa'), ['a', 'aa'])
        self.assertEqual(permute_string('aaa'), ['a', 'aa', 'aaa'])

    def test_special_characters(self):
        self.assertEqual(permute_string('A!@#$%^&*()'), [
            'A', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 'A!', 'A!@', 'A!@#', 'A!@#$', 'A!@#$%',
            'A!@#$%^', 'A!@#$%^&', 'A!@#$%^&*', 'A!@#$%^&*(', 'A!(', 'A!)', 'A)!', 'A)!@', 'A)!@#', 'A)!@#$',
            'A)!@#$%', 'A)!@#$%^', 'A)!@#$%^&', 'A)!@#$%^&*', 'A)!@#$%^&*(', 'A)!(', 'A)!@', 'A)!@#', 'A)!@#$',
            'A)!@#$%', 'A)!@#$%^', 'A)!@#$%^&', 'A)!@#$%^&*', 'A)!@#$%^&*(', 'A@', '@A', '@A!', '@A!@', '@A!@#',
            '@A!@#$', '@A!@#$%', '@A!@#$%^', '@A!@#$%^&', '@A!@#$%^&*', '@A!@#$%^&*(', '@A@', '@A!', '@A!@',
            '@A!@#', '@A!@#$', '@A!@#$%', '@A!@#$%^', '@A!@#$%^&', '@A!@#$%^&*', '@A!@#$%^&*(', '@A@', '@A!',
            '@A!@', '@A!@#', '@A!@#$', '@A!@#$%', '@A!@#$%^', '@A!@#$%^&', '@A!@#$%^&*', '@A!@
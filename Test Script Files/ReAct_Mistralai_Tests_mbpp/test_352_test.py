import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_empty_string(self):
        """Test if the function correctly handles an empty string"""
        self.assertTrue(unique_Characters(""))

    def test_single_character_string(self):
        """Test if the function correctly handles a string with one character"""
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(unique_Characters(char))

    def test_multiple_unique_characters(self):
        """Test if the function correctly handles a string with multiple unique characters"""
        for string in ['abc', '123', '!@#', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '0123456789', '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/~`', 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:'\'<>,.?/~`']:
            self.assertTrue(unique_Characters(string))

    def test_duplicate_characters_at_start(self):
        """Test if the function correctly handles a string with duplicate characters at the start"""
        for char in 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv':
            self.assertFalse(unique_Characters(char*2))

    def test_duplicate_characters_in_middle(self):
        """Test if the function correctly handles a string with duplicate characters in the middle"""
        for string in ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'oooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv'):
            self.assertFalse(unique_Characters(string))

    def test_duplicate_characters_at_end(self):
        """Test if the function correctly handles a string with duplicate characters at the end"""
        for string in ('aaZ', 'bbY', 'ccX', 'ddW', 'eeV', 'ffU', 'ggT', 'hhS', 'iiiR', 'jjjQ', 'kkkP', 'lllO', 'mmmN', 'nnnM', 'ooooL', 'pppK', 'qqqJ', 'rrrI', 'sssH', 'tttG', 'uuuF', 'vvvE'):
            self.assertFalse(unique_Characters(string))

    def test_duplicate_characters_in_middle_and_end(self):
        """Test if the function correctly handles a string with duplicate characters in the middle and at the end"""
        for string in ('aaaZ', 'bbbY', 'cccX', 'dddW', 'eeeV', 'fffU', 'gggT', 'hhhS', 'iiiR', 'jjjQ', 'kkkP', 'lllO', 'mmmN', 'nnnM', 'ooooL', 'pppK', 'qqqJ', 'rrrI', 'sssH', 'tttG', 'uuuF', 'vvvE'):
            self.assertFalse(unique_Characters(string))

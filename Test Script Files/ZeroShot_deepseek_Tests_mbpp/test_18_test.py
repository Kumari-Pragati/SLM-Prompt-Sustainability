import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_remove_dirty_chars(self):
        self.assertEqual(remove_dirty_chars('abc', ''), 'abc')
        self.assertEqual(remove_dirty_chars('abc', 'a'), 'bc')
        self.assertEqual(remove_dirty_chars('abc', 'b'), 'ac')
        self.assertEqual(remove_dirty_chars('abc', 'c'), 'ab')
        self.assertEqual(remove_dirty_chars('abc', 'd'), 'abc')
        self.assertEqual(remove_dirty_chars('abc', 'abcd'), '')
        self.assertEqual(remove_dirty_chars('abc', 'abc'), '')
        self.assertEqual(remove_dirty_chars('abc', 'cba'), 'a')
        self.assertEqual(remove_dirty_chars('abc', 'cab'), 'b')
        self.assertEqual(remove_dirty_chars('abc', 'bac'), 'c')
        self.assertEqual(remove_dirty_chars('abc', 'abcabc'), 'abc')
        self.assertEqual(remove_dirty_chars('abc', 'abcabcabc'), '')

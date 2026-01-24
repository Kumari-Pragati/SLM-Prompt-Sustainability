import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_find_longest_repeating_subseq(self):
        self.assertEqual(find_longest_repeating_subseq('aab'), 2)
        self.assertEqual(find_longest_repeating_subseq('aabb'), 2)
        self.assertEqual(find_longest_repeating_subseq('aabba'), 3)
        self.assertEqual(find_longest_repeating_subseq('aabbcc'), 2)
        self.assertEqual(find_longest_repeating_subseq('abc'), 0)
        self.assertEqual(find_longest_repeating_subseq('aaaa'), 2)
        self.assertEqual(find_longest_repeating_subseq(''), 0)

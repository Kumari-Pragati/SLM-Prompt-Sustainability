import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_no_duplicates(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_duplicates(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 4, 4], 6), 2)

    def test_duplicates_at_start(self):
        self.assertEqual(count_Pairs([1, 1, 2, 3, 4, 4], 6), 2)

    def test_duplicates_at_end(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 4, 4], 6), 2)

    def test_duplicates_spaced(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 5], 6), 1)

    def test_duplicates_everywhere(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 6)

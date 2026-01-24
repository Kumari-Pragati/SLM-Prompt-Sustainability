import unittest
from564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_two_elements_same(self):
        self.assertEqual(count_Pairs([1, 1], 2), 0)

    def test_two_elements_different(self):
        self.assertEqual(count_Pairs([1, 2], 2), 1)

    def test_multiple_elements_same(self):
        self.assertEqual(count_Pairs([1, 1, 1], 3), 0)

    def test_multiple_elements_different(self):
        self.assertEqual(count_Pairs([1, 2, 3], 3), 2)

    def test_duplicates_in_middle(self):
        self.assertEqual(count_Pairs([1, 2, 1, 3], 4), 1)

    def test_duplicates_at_end(self):
        self.assertEqual(count_Pairs([1, 2, 1], 3), 1)

import unittest
from mbpp_172_code import count_occurance

class TestCountOccurrence(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_occurance(''), 0)

    def test_single_occurrence(self):
        self.assertEqual(count_occurance('std'), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_occurance('stdstd'), 2)

    def test_occurrence_at_beginning(self):
        self.assertEqual(count_occurance('stdabcstd'), 2)

    def test_occurrence_at_end(self):
        self.assertEqual(count_occurance('abcsstd'), 1)

    def test_occurrence_in_middle(self):
        self.assertEqual(count_occurance('abcsstdabc'), 1)

    def test_occurrence_with_spaces(self):
        self.assertEqual(count_occurance('std std'), 1)

    def test_occurrence_with_other_characters(self):
        self.assertEqual(count_occurance('stxstd'), 1)

    def test_occurrence_with_longer_substrings(self):
        self.assertEqual(count_occurance('stdistd'), 1)

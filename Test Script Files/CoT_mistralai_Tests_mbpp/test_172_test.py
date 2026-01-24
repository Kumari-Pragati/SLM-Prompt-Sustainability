import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_occurance(''), 0)

    def test_single_occurance(self):
        self.assertEqual(count_occurance('std'), 1)

    def test_multiple_occurances(self):
        self.assertEqual(count_occurance('stdstd'), 2)

    def test_occurance_at_end(self):
        self.assertEqual(count_occurance('stds'), 0)

    def test_occurance_at_beginning(self):
        self.assertEqual(count_occurance('sstd'), 0)

    def test_occurance_in_middle(self):
        self.assertEqual(count_occurance('stdsst'), 1)

    def test_occurance_with_extra_characters(self):
        self.assertEqual(count_occurance('sstdd'), 0)

    def test_occurance_with_non_matching_characters(self):
        self.assertEqual(count_occurance('stft'), 0)

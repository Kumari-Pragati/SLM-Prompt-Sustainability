import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(find_adverb_position(''))

    def test_single_adverb(self):
        self.assertEqual(find_adverb_position('quickly'), (3, 7, 'quickly'))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position('slowly and quickly'), (6, 13, 'quickly'))

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverb_position('quickly text'), (0, 5, 'quickly'))

    def test_adverb_at_end(self):
        self.assertEqual(find_adverb_position('text quickly'), (17, 23, 'quickly'))

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverb_position('text slowly quickly'), (10, 20, 'quickly'))

    def test_adverb_with_hyphen(self):
        self.assertEqual(find_adverb_position('text very-quickly'), (10, 21, 'very-quickly'))

    def test_adverb_with_apostrophe(self):
        self.assertEqual(find_adverb_position("O'Connor's quickly"), (13, 24, 'quickly'))

    def test_adverb_with_number(self):
        self.assertEqual(find_adverb_position('text twice quickly'), (10, 23, 'quickly'))

    def test_adverb_with_special_characters(self):
        self.assertEqual(find_adverb_position('text!@#$%quickly'), (10, 23, 'quickly'))

    def test_non_adverb_word(self):
        self.assertIsNone(find_adverb_position('text only'))

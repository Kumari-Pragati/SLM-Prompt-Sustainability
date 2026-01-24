import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate('hello world hello'), 'hello world')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_no_duplicate(self):
        self.assertEqual(remove_duplicate('the quick brown fox jumps'), 'the quick brown fox jumps')

    def test_duplicate_at_end(self):
        self.assertEqual(remove_duplicate('the quick brown fox jumps fox'), 'the quick brown fox jumps')

    def test_duplicate_at_start(self):
        self.assertEqual(remove_duplicate('fox the quick brown fox jumps'), 'fox the quick brown jumps')

    def test_duplicate_in_middle(self):
        self.assertEqual(remove_duplicate('the quick brown fox jumps fox'), 'the quick brown fox jumps')

    def test_duplicate_with_special_characters(self):
        self.assertEqual(remove_duplicate('the quick brown! fox, jumps. fox;'), 'the quick brown! fox, jumps.')

    def test_duplicate_with_numbers(self):
        self.assertEqual(remove_duplicate('the 1 quick 2 brown 3 fox 4 jumps 5 fox 6'), 'the 1 quick 2 brown 3 fox 4 jumps 5')

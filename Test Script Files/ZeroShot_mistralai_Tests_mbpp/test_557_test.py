import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(toggle_string(''), '')

    def test_single_uppercase_letter(self):
        self.assertEqual(toggle_string('A'), 'a')

    def test_single_lowercase_letter(self):
        self.assertEqual(toggle_string('a'), 'A')

    def test_mixed_case_string(self):
        self.assertEqual(toggle_string('Hello World'), 'hELLO wORLD')

    def test_special_characters(self):
        self.assertEqual(toggle_string('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:"\'>,.<>?/')

    def test_punctuation_at_start_and_end(self):
        self.assertEqual(toggle_string('.,;:!"\'\@#$%^&*()_+-=[]{}|;:<>,.?'), ',.;:!"\'\@#$%^&*()_+-=[]{}|;:>><,>.?')

import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_two_three('abababc'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_two_three('abcabab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_two_three('abababab'), 'Found a match!')

    def test_match_found_at_start_and_end(self):
        self.assertEqual(text_match_two_three('ababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_multiple_times(self):
        self.assertEqual(text_match_two_three('ababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle(self):
        self.assertEqual(text_match_two_three('abababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_multiple_times(self):
        self.assertEqual(text_match_two_three('abababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(text_match_two_three('ababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_multiple_times(self):
        self.assertEqual(text_match_two_three('ababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(text_match_two_three('abababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_multiple_times(self):
        self.assertEqual(text_match_two_three('abababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(text_match_two_three('ababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_multiple_times(self):
        self.assertEqual(text_match_two_three('ababababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(text_match_two_three('abababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_multiple_times(self):
        self.assertEqual(text_match_two_three('abababababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(text_match_two_three('ababababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_multiple_times(self):
        self.assertEqual(text_match_two_three('ababababababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(text_match_two_three('abababababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_multiple_times(self):
        self.assertEqual(text_match_two_three('abababababababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(text_match_two_three('ababababababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_multiple_times(self):
        self.assertEqual(text_match_two_three('ababababababababababababab'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(text_match_two_three('abababababababababababababc'), 'Found a match!')

    def test_match_found_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_multiple_times(self):
        self.assertEqual(text_match_two_three('abababababababababababababab'),
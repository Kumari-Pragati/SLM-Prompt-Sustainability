import unittest
from mbpp_11_code import remove_Occ

class TestRemove_Occ(unittest.TestCase):
    def test_remove_single_occurrence(self):
        self.assertEqual(remove_Occ("hello", "o"), "hell")

    def test_remove_single_occurrence_at_start(self):
        self.assertEqual(remove_Occ("ocean", "o"), "cean")

    def test_remove_single_occurrence_at_end(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_remove_multiple_occurrences(self):
        self.assertEqual(remove_Occ("hellooo", "o"), "hell")

    def test_remove_multiple_occurrences_at_start(self):
        self.assertEqual(remove_Occ("oceanoo", "o"), "cean")

    def test_remove_multiple_occurrences_at_end(self):
        self.assertEqual(remove_Occ("helloooo", "o"), "hell")

    def test_remove_occurrence_not_found(self):
        self.assertEqual(remove_Occ("hello", "z"), "hello")

    def test_remove_occurrence_not_found_at_start(self):
        self.assertEqual(remove_Occ("hello", "H"), "hello")

    def test_remove_occurrence_not_found_at_end(self):
        self.assertEqual(remove_Occ("hello", "L"), "hello")

import unittest
from172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_occurance(""), 0)

    def test_single_occurance(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_multiple_occurances(self):
        self.assertEqual(count_occurance("stddstdd"), 2)

    def test_case_sensitive(self):
        self.assertEqual(count_occurance("StD"), 0)

    def test_start_and_end_edge_cases(self):
        self.assertEqual(count_occurance("s"), 0)
        self.assertEqual(count_occurance("stdt"), 1)

    def test_long_string(self):
        long_string = "std" * 1000 + "t" * 1000 + "d" * 1000
        self.assertEqual(count_occurance(long_string), 1000)

    def test_non_matching_sequence(self):
        self.assertEqual(count_occurance("sss"), 0)

import unittest
from mbpp_684_code import count_Char

class TestCount_Char(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Char("hello", "l"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_Char("a", "a"), 1)

    def test_edge_case_single_char_string_with_repetitions(self):
        self.assertEqual(count_Char("a", "a"), 10)

    def test_edge_case_single_char_string_with_repetitions_and_remainder(self):
        self.assertEqual(count_Char("a", "a"), 11)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_end(self):
        self.assertEqual(count_Char("a", "a"), 12)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start(self):
        self.assertEqual(count_Char("a", "a"), 13)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_middle(self):
        self.assertEqual(count_Char("abc", "a"), 5)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 6)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 7)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_end_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 8)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 9)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_Char("abc", "a"), 10)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 11)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 12)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 13)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_Char("abc", "a"), 14)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 15)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 16)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 17)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_Char("abc", "a"), 18)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 19)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(count_Char("abc", "a"), 20)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(count_Char("abc", "a"), 21)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(count_Char("abc", "a"), 22)

    def test_edge_case_single_char_string_with_re
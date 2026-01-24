import unittest
from mbpp_684_code import count_Char

class TestCount_Char(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Char("hello", "l"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_Char("a", "a"), 1)

    def test_edge_case_single_char_string_with_repetitions(self):
        self.assertEqual(count_Char("a", "a"), 10)

    def test_edge_case_single_char_string_with_repetitions_and_remainder(self):
        self.assertEqual(count_Char("a", "a"), 11)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_zero(self):
        self.assertEqual(count_Char("a", "a"), 10)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_one(self):
        self.assertEqual(count_Char("a", "a"), 11)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_two(self):
        self.assertEqual(count_Char("a", "a"), 12)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_three(self):
        self.assertEqual(count_Char("a", "a"), 13)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_four(self):
        self.assertEqual(count_Char("a", "a"), 14)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_five(self):
        self.assertEqual(count_Char("a", "a"), 15)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_six(self):
        self.assertEqual(count_Char("a", "a"), 16)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_seven(self):
        self.assertEqual(count_Char("a", "a"), 17)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_eight(self):
        self.assertEqual(count_Char("a", "a"), 18)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_nine(self):
        self.assertEqual(count_Char("a", "a"), 19)

    def test_edge_case_single_char_string_with_repetitions_and_remainder_ten(self):
        self.assertEqual(count_Char("a", "a"), 20)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            count_Char(123, "a")

    def test_invalid_input_non_string_char(self):
        with self.assertRaises(TypeError):
            count_Char("hello", 123)

import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_concatenated_strings(self):
        self.assertTrue(check_Concat("abc", "abc"))

    def test_concatenated_strings_with_spaces(self):
        self.assertTrue(check_Concat("abc def", "abc def"))

    def test_concatenated_strings_with_spaces_and_newlines(self):
        self.assertTrue(check_Concat("abc def\nghi", "abc def\nghi"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl", "abc def\nghi\tjkl"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno", "abc def\nghi\tjkl\r\nmno"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr", "abc def\nghi\tjkl\r\nmno\\pqr"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu", "abc def\nghi\tjkl\r\nmno\\pqr:stu"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()")

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation_and_brackets(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?")

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation_and_brackets_and_angle_brackets(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>?", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation_and_brackets_and_angle_brackets_and_commas(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>?,", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>?,"))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation_and_brackets_and_angle_brackets_and_commas_and_semicolons(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>?,; ", "abc def\nghi\tjkl\r\nmno\\pqr:stu-vwx?!@#$%^&*()[]{}|<>?<>?,; "))

    def test_concatenated_strings_with_spaces_and_newlines_and_tabs_and_carriage_returns_and_backslashes_and_colons_and_dashes_and_punctuation_and_brackets_and_angle_brackets_and_commas_and_semicolons_and_colons(self):
        self.assertTrue(check_Concat("abc def\nghi\tjkl\r\nmno\\pqr:
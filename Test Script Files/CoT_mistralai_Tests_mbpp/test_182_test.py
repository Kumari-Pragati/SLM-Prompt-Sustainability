import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_character(""), ([], [], [], []))

    def test_only_uppercase(self):
        self.assertEqual(find_character("ABC"), (["A", "B", "C"], [], [], [" ", ""]))

    def test_only_lowercase(self):
        self.assertEqual(find_character("abc"), ([], ["a", "b", "c"], [], [" ", ""]))

    def test_only_numbers(self):
        self.assertEqual(find_character("123"), ([], [], ["1", "2", "3"], [" ", ""]))

    def test_only_special_characters(self):
        self.assertEqual(find_character("!@#$%^&*()"), ([], [], [], ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ""]))

    def test_mixed_case(self):
        self.assertEqual(find_character("AbC123!@#"), (["A", "B", "C"], ["a"], ["1", "2", "3"], ["!", "@", "#"]))

    def test_long_string(self):
        long_string = "A" * 100 + "B" * 100 + "1" * 100 + "2" * 100 + "!" * 100 + "@" * 100 + "#" * 100
        self.assertEqual(find_character(long_string), (list(set(long_string))), "Long string should not cause issues")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_character(123)

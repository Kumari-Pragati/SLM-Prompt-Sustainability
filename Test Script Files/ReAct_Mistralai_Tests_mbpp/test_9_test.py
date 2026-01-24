import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_single_character(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEqual(find_Rotations(char), 1)

    def test_two_characters(self):
        for pair in [("AA", 1), ("AB", 2), ("BA", 2)]:
            self.assertEqual(find_Rotations(pair[0]), pair[1])

    def test_longer_strings(self):
        for text in ["ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG"]:
            self.assertLessEqual(find_Rotations(text), len(text))

    def test_rotations(self):
        for text in ["ABC", "CAB", "BCA"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_longer(self):
        for text in ["ABCDEFG", "GDEFGABC", "FGABCDEF"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_with_different_case(self):
        for text in ["AbCdEfGhIjKlMnOpQrStUvWxYz", "zYxWvUqRsTpOnLkJiHgFeDcBa"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_with_spaces(self):
        for text in ["Hello World", "World Hello"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_with_special_characters(self):
        for text in ["!@#$%^&*()_+-=[]{}|;:'\",.<>?ABC", "ABC!@#$%^&*()_+-=[]{}|;:'\",.<>?"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_with_numbers(self):
        for text in ["1234567890ABC", "ABC1234567890"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_rotations_with_mixed_types(self):
        for text in ["123ABC", "ABC123", "123\nABC", "ABC\n123"]:
            self.assertEqual(find_Rotations(text), 1)

    def test_no_rotations(self):
        self.assertEqual(find_Rotations("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 27)

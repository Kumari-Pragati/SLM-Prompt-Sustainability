import unittest
from914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_Two_Alter(""))

    def test_single_char_string(self):
        for char in ['a', 'b', 'c']:
            self.assertFalse(is_Two_Alter(char))

    def test_two_char_string(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['a', 'b', 'c']:
                self.assertFalse(is_Two_Alter(char1 + char2))

    def test_three_char_string_same_first_and_second(self):
        for char1 in ['a', 'b', 'c']:
            self.assertFalse(is_Two_Alter(char1 + 'x' + char1))

    def test_three_char_string_same_first_and_third(self):
        for char1 in ['a', 'b', 'c']:
            self.assertFalse(is_Two_Alter(char1 + 'x' + char1))

    def test_three_char_string_different(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['d', 'e', 'f']:
                for char3 in ['g', 'h', 'i']:
                    if char1 != char3:
                        self.assertTrue(is_Two_Alter(char1 + char2 + char3))

    def test_four_char_string_same_first_and_second(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['d', 'e', 'f']:
                self.assertFalse(is_Two_Alter(char1 + char2 + char1 + char2))

    def test_four_char_string_same_first_and_third(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['d', 'e', 'f']:
                self.assertFalse(is_Two_Alter(char1 + char2 + char1 + char2))

    def test_four_char_string_same_second_and_third(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['d', 'e', 'f']:
                self.assertFalse(is_Two_Alter(char1 + char2 + char2 + char1))

    def test_four_char_string_different(self):
        for char1 in ['a', 'b', 'c']:
            for char2 in ['d', 'e', 'f']:
                for char3 in ['g', 'h', 'i']:
                    for char4 in ['j', 'k', 'l']:
                        if char1 != char3 and char2 != char4:
                            self.assertTrue(is_Two_Alter(char1 + char2 + char3 + char4))

    def test_longer_string(self):
        for length in range(5, 10):
            sequence = ''.join(chr(ord('a') + i) for i in range(length))
            self.assertTrue(is_Two_Alter(sequence))

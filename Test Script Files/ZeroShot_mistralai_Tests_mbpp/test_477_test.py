import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_lower(''), True)

    def test_single_uppercase_letter(self):
        for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            self.assertEqual(is_lower(char), False)

    def test_single_lowercase_letter(self):
        for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            self.assertEqual(is_lower(char), True)

    def test_mixed_case_string(self):
        for test_string in ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'aBcDeFgHiJkLmNoPqRsTuVwXyZ', 'AbCdEfGhIjKlMnOpQrStUvWxYz123', 'aBcDeFgHiJkLmNoPqRsTuVwXyZ456']:
            self.assertEqual(is_lower(test_string), False)

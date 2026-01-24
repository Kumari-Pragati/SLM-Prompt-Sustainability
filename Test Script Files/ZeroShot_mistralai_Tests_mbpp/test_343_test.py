import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(dig_let(''), (0, 0))

    def test_all_digits(self):
        self.assertEqual(dig_let('12345'), (0, 5))

    def test_all_letters(self):
        self.assertEqual(dig_let('abcdefg'), (7, 0))

    def test_mixed_case(self):
        self.assertEqual(dig_let('AbCd123Ef456'), (6, 4))

    def test_special_characters(self):
        self.assertEqual(dig_let('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), (0, 0))

    def test_whitespace(self):
        self.assertEqual(dig_let(' Hello World 123 '), (7, 3))

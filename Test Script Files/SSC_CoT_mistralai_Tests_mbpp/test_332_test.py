import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):
    def test_normal_input(self):
        self.assertDictEqual(char_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 2})
        self.assertDictEqual(char_frequency("Python"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1})

    def test_edge_cases(self):
        self.assertDictEqual(char_frequency(""), {})
        self.assertDictEqual(char_frequency("a"), {'a': 1})
        self.assertDictEqual(char_frequency("aaa"), {'a': 3})
        self.assertDictEqual(char_frequency("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), {c: 1 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"})

    def test_special_cases(self):
        self.assertDictEqual(char_frequency("Hello, World!"), {' ': 1, 'H': 1, 'e': 1, 'l': 2, ',': 1, 'W': 1, 'o': 1, 'r': 1, 'd': 1, '!': 1})
        self.assertDictEqual(char_frequency("12345"), {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1})
        self.assertDictEqual(char_frequency("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '_': 1, '-': 1, '+': 1, '=': 1, '[': 1, ']': 1, '{': 1, '}': 1, '|': 1, ';': 1, ':': 1, "'": 1, '"': 1, '<': 1, '>': 1, '?': 1, '/': 1})

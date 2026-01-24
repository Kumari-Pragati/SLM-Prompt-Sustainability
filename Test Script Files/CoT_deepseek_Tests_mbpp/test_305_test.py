import unittest
from mbpp_305_code import start_withp

class TestStartsWithP(unittest.TestCase):

    def test_typical_case(self):
        words = ["Panda loves playing", "Penguin is a bird"]
        self.assertEqual(start_withp(words), ('Panda', 'Penguin'))

    def test_single_word_with_p(self):
        words = ["Panda"]
        self.assertIsNone(start_withp(words))

    def test_no_words(self):
        words = []
        self.assertIsNone(start_withp(words))

    def test_words_without_p(self):
        words = ["Elephant is a mammal", "Lion is a cat"]
        self.assertIsNone(start_withp(words))

    def test_words_with_multiple_p(self):
        words = ["PPanda loves playing", "Penguin is a PP"]
        self.assertEqual(start_withp(words), ('PPanda', 'Penguin'))

    def test_words_with_special_characters(self):
        words = ["Panda@ loves playing", "Penguin! is a bird"]
        self.assertEqual(start_withp(words), ('Panda@', 'Penguin!'))

    def test_words_with_numbers(self):
        words = ["Panda1 loves playing", "Penguin2 is a bird"]
        self.assertEqual(start_withp(words), ('Panda1', 'Penguin2'))

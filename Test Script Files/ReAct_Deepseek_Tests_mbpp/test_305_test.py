import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):

    def test_typical_case(self):
        words = ["Panda loves playing", "Penguin is a bird"]
        self.assertEqual(start_withp(words), ('Panda', 'Penguin'))

    def test_edge_case_single_word(self):
        words = ["Penguin is a bird"]
        self.assertIsNone(start_withp(words))

    def test_edge_case_no_words(self):
        words = []
        self.assertIsNone(start_withp(words))

    def test_edge_case_no_match(self):
        words = ["Lion is a wild animal", "Elephant is a big animal"]
        self.assertIsNone(start_withp(words))

    def test_error_case_non_string_input(self):
        words = ["Panda loves playing", 123]
        with self.assertRaises(TypeError):
            start_withp(words)

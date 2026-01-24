import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_typical_use_case(self):
        words = ["Penguin is a bird", "Pineapple is a fruit", "Pecan is a nut"]
        self.assertEqual(start_withp(words), ("Penguin", "bird"))

    def test_multiple_matches(self):
        words = ["Penguin is a bird", "Pineapple is a fruit", "Pecan is a nut", "Peach is a fruit"]
        self.assertEqual(start_withp(words), ("Penguin", "bird"))

    def test_no_matches(self):
        words = ["apple is a fruit", "banana is a fruit", "cherry is a fruit"]
        self.assertIsNone(start_withp(words))

    def test_empty_input(self):
        words = []
        self.assertIsNone(start_withp(words))

    def test_single_word(self):
        words = ["Penguin"]
        self.assertIsNone(start_withp(words))

    def test_non_string_input(self):
        words = [1, 2, 3]
        with self.assertRaises(TypeError):
            start_withp(words)

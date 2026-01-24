import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):
    def test_valid_input_with_two_matches(self):
        self.assertEqual(start_withp(["Pab", "Pqr"]), ("Pab", "Pqr"))

    def test_valid_input_with_one_match(self):
        self.assertEqual(start_withp(["Pab"]), ("Pab", None))

    def test_valid_input_with_no_matches(self):
        self.assertEqual(start_withp(["abc", "def"]), (None, None))

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            start_withp([])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            start_withp([1, 2, 3])

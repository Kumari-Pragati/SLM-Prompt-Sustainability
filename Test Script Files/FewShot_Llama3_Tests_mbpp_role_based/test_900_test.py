import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_num_start_with_5(self):
        self.assertTrue(match_num("5hello"))

    def test_match_num_no_match(self):
        self.assertFalse(match_num("hello"))

    def test_match_num_empty_string(self):
        self.assertFalse(match_num(""))

    def test_match_num_non_string_input(self):
        with self.assertRaises(TypeError):
            match_num(123)

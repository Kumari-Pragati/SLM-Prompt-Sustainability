import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_num_true(self):
        self.assertTrue(match_num("5"))

    def test_match_num_false(self):
        self.assertFalse(match_num("6"))

    def test_match_num_empty(self):
        self.assertFalse(match_num(""))

    def test_match_num_non_string(self):
        with self.assertRaises(TypeError):
            match_num(123)

    def test_match_num_non_match(self):
        self.assertFalse(match_num("123"))

    def test_match_num_match(self):
        self.assertTrue(match_num("5abc"))

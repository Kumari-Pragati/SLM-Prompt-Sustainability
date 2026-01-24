import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_num_true(self):
        self.assertTrue(match_num("5hello"))

    def test_match_num_false(self):
        self.assertFalse(match_num("hello"))

    def test_match_num_edge_case(self):
        self.assertTrue(match_num("5"))

    def test_match_num_edge_case2(self):
        self.assertFalse(match_num(""))

    def test_match_num_invalid_input(self):
        with self.assertRaises(TypeError):
            match_num(None)

    def test_match_num_invalid_input2(self):
        with self.assertRaises(TypeError):
            match_num("")

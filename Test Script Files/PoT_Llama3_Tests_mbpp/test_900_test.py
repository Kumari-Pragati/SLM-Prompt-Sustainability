import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_typical_match(self):
        self.assertTrue(match_num("5"))

    def test_typical_non_match(self):
        self.assertFalse(match_num("6"))

    def test_edge_match(self):
        self.assertTrue(match_num("50"))

    def test_edge_non_match(self):
        self.assertFalse(match_num("3"))

    def test_boundary_match(self):
        self.assertTrue(match_num("500"))

    def test_boundary_non_match(self):
        self.assertFalse(match_num("999"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            match_num(None)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            match_num("")

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            match_num(123)

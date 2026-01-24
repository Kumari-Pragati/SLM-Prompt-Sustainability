import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(start_withp(["PP1", "ABC", "P23", "XYZ"]), ("PP1", "P23"))

    def test_edge_case_short_word(self):
        self.assertEqual(start_withp(["P", "ABC"]), None)

    def test_edge_case_long_word(self):
        self.assertEqual(start_withp(["PP123456", "ABC"]), None)

    def test_edge_case_no_match(self):
        self.assertEqual(start_withp(["ABC", "XYZ"]), None)

    def test_corner_case_empty_list(self):
        self.assertEqual(start_withp([]), None)

    def test_corner_case_single_word(self):
        self.assertEqual(start_withp(["PP1"]), ("PP1", None))

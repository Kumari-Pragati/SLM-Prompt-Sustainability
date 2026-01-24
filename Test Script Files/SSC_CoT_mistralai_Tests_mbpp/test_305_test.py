import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(start_withp(["PP1", "P2", "NonP"]), ("PP1", "P2"))

    def test_edge_case_short(self):
        self.assertIsNone(start_withp(["P"]))

    def test_edge_case_long(self):
        self.assertIsNone(start_withp(["P123456789"]))

    def test_edge_case_empty(self):
        self.assertIsNone(start_withp([]))

    def test_case_with_numbers(self):
        self.assertIsNone(start_withp(["P1", "P23", "NonP"]))

    def test_case_with_special_characters(self):
        self.assertIsNone(start_withp(["P!", "P@", "NonP"]))

    def test_case_with_multiple_matches(self):
        self.assertIsNone(start_withp(["PP1", "P2P", "NonP"]))

    def test_case_with_only_one_match(self):
        self.assertEqual(start_withp(["P1", "NonP", "P"]), ("P1", None))

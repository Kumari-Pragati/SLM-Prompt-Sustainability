import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(start_withp(["PP1", "ABC", "P23", "XYZ"]), ("PP1", "P23"))

    def test_edge_case_single_word(self):
        self.assertIsNone(start_withp(["P"]))

    def test_edge_case_no_match(self):
        self.assertIsNone(start_withp(["ABC", "XYZ"]))

    def test_edge_case_empty_list(self):
        self.assertIsNone(start_withp([]))

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, start_withp, [1, 2, 3])

    def test_invalid_input_non_string_element(self):
        self.assertRaises(TypeError, start_withp, ["P", 1, "P23"])

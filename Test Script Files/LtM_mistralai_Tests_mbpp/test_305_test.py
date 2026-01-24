import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(start_withp(["PP1", "QWERT", "P23"]), ("PP1", "P23"))

    def test_edge_case_min(self):
        self.assertEqual(start_withp(["P", "PP1"]), None)

    def test_edge_case_max(self):
        self.assertEqual(start_withp(["PP123", "QWERT"]), None)

    def test_boundary_case_spaces(self):
        self.assertEqual(start_withp(["PP1 ", "QWERT"]), None)

    def test_boundary_case_special_chars(self):
        self.assertEqual(start_withp(["PP1!", "QWERT"]), None)

    def test_complex_case_mixed_words(self):
        self.assertEqual(start_withp(["PP1QWERT", "P23QWERTY"]), None)

    def test_invalid_input_empty_list(self):
        self.assertEqual(start_withp([]), None)

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, start_withp, [1, 2, 3])

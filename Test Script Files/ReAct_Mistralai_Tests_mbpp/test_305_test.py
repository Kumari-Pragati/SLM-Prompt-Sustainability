import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(start_withp(["P123", "Q456"]), ("P123", "Q"))

    def test_edge_case_single_word(self):
        self.assertIsNone(start_withp(["P"]))

    def test_edge_case_no_match(self):
        self.assertIsNone(start_withp(["Q123", "R456"]))

    def test_edge_case_empty_list(self):
        self.assertIsNone(start_withp([]))

    def test_error_case_non_string(self):
        with self.assertRaises(TypeError):
            start_withp([1, 2, 3])

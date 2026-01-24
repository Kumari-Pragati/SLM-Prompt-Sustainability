import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_typical_yes(self):
        self.assertEqual(check("101"), "Yes")

    def test_typical_no(self):
        self.assertEqual(check("111111"), "No")

    def test_edge_case_zero(self):
        self.assertEqual(check("000"), "Yes")

    def test_edge_case_one(self):
        self.assertEqual(check("111"), "Yes")

    def test_edge_case_mixed(self):
        self.assertEqual(check("101010"), "No")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check(None)

    def test_empty_string(self):
        self.assertEqual(check(""), "No")

    def test_single_character(self):
        self.assertEqual(check("1"), "Yes")

    def test_multiple_characters(self):
        self.assertEqual(check("110"), "Yes")

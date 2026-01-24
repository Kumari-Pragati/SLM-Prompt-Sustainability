import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_typical_valid(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_typical_invalid(self):
        self.assertEqual(check_str("123"), "Invalid")

    def test_edge_start_uppercase(self):
        self.assertEqual(check_str("AHello"), "Valid")

    def test_edge_start_lowercase(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_non_alphabetic(self):
        self.assertEqual(check_str("1Hello"), "Invalid")

    def test_edge_end_non_alphabetic(self):
        self.assertEqual(check_str("aHello1"), "Valid")

    def test_edge_middle_non_alphabetic(self):
        self.assertEqual(check_str("aHe11o"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello1"), "Invalid")

    def test_edge_start_end_alphabetic(self):
        self.assertEqual(check_str("aHello"), "Valid")

    def test_edge_start_end_non_alphabetic(self):
        self.assertEqual(check_str("a1Hello
import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_str("A"), "Valid")
        self.assertEqual(check_str("Alphab3t"), "Valid")
        self.assertEqual(check_str("αβγδεζη"), "Valid")

    def test_edge_cases(self):
        self.assertEqual(check_str("A_"), "Valid")
        self.assertEqual(check_str("A_1"), "Invalid")
        self.assertEqual(check_str("1A"), "Invalid")
        self.assertEqual(check_str("_A"), "Invalid")
        self.assertEqual(check_str("A "), "Invalid")
        self.assertEqual(check_str("A\t"), "Invalid")
        self.assertEqual(check_str("A\n"), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_str(""), "Invalid")

    def test_special_characters(self):
        self.assertEqual(check_str("A#"), "Invalid")
        self.assertEqual(check_str("A@"), "Invalid")
        self.assertEqual(check_str("A$"), "Invalid")
        self.assertEqual(check_str("A%"), "Invalid")
        self.assertEqual(check_str("A&"), "Invalid")
        self.assertEqual(check_str("A*"), "Invalid")
        self.assertEqual(check_str("A("), "Invalid")
        self.assertEqual(check_str("A)"), "Invalid")
        self.assertEqual(check_str("A+"), "Invalid")
        self.assertEqual(check_str("A,"), "Invalid")
        self.assertEqual(check_str("A;"), "Invalid")
        self.assertEqual(check_str("A="), "Invalid")
        self.assertEqual(check_str("A'"), "Invalid")
        self.assertEqual(check_str("A["), "Invalid")
        self.assertEqual(check_str("A]"), "Invalid")
        self.assertEqual(check_str("A\\"), "Invalid")
        self.assertEqual(check_str("A|"), "Invalid")
        self.assertEqual(check_str("A{"), "Invalid")
        self.assertEqual(check_str("A}"), "Invalid")
        self.assertEqual(check_str("A~"), "Invalid")

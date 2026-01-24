import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_str("A1bCdEf_Gh"), "Valid")
        self.assertEqual(check_str("a1bCdEf_Gh"), "Valid")
        self.assertEqual(check_str("Ae1bCdEf_Gh"), "Valid")
        self.assertEqual(check_str("Ae1bCdEf_GhIJ"), "Valid")

    def test_invalid_string(self):
        self.assertEqual(check_str("123"), "Invalid")
        self.assertEqual(check_str("1Ae1bCdEf_Gh"), "Invalid")
        self.assertEqual(check_str("Ae1bCdEf_GhIJK"), "Invalid")
        self.assertEqual(check_str(""), "Invalid")
        self.assertEqual(check_str(" "), "Invalid")
        self.assertEqual(check_str("A"), "Invalid")
        self.assertEqual(check_str("Ae"), "Invalid")
        self.assertEqual(check_str("Ae1bCdEf_GhIJK_"), "Invalid")
        self.assertEqual(check_str("Ae1bCdEf_GhIJK_1"), "Invalid")

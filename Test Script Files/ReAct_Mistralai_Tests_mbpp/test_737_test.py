import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_str("A1bCdEf"), "Valid")
        self.assertEqual(check_str("a1bCdEf"), "Valid")
        self.assertEqual(check_str("A1_bCdEf"), "Valid")
        self.assertEqual(check_str("A1bCd_Ef"), "Valid")
        self.assertEqual(check_str("A1bCdEf_"), "Valid")

    def test_invalid_string(self):
        self.assertEqual(check_str("123"), "Invalid")
        self.assertEqual(check_str("1A1bCdEf"), "Invalid")
        self.assertEqual(check_str("A!bCdEf"), "Invalid")
        self.assertEqual(check_str("A1bCdEf!"), "Invalid")
        self.assertEqual(check_str("A1bCdEf_!"), "Invalid")
        self.assertEqual(check_str(""), "Invalid")
        self.assertEqual(check_str(None), "Invalid")

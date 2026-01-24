import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")
        self.assertEqual(check_email("test_123@example.co.uk"), "Valid Email")
        self.assertEqual(check_email("test.123@example.com"), "Valid Email")
        self.assertEqual(check_email("test123@example.com"), "Valid Email")
        self.assertEqual(check_email("test_123@example.org"), "Valid Email")
        self.assertEqual(check_email("test_123@example.net"), "Valid Email")
        self.assertEqual(check_email("test_123@example.edu"), "Valid Email")
        self.assertEqual(check_email("test_123@example.gov"), "Valid Email")
        self.assertEqual(check_email("test_123@example.mil"), "Valid Email")
        self.assertEqual(check_email("test_123@example.int"), "Valid Email")

    def test_edge_cases(self):
        self.assertEqual(check_email("test@example.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.a"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aa"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aA"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aAa"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaa"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaA"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAa"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaa"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaA"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.c"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.cc"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.d"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.dd"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.ddd"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.ddd.e"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.ddd.ee"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.aaaAaaAb.ccc.ddd.eee"), "Invalid Email")

    def test_special_cases(self):
        self.assertEqual(check_email("test_123@example.com.example"), "Invalid Email")
        self.assertEqual(check_email("test_123@example.com.example.com"), "Invalid Email")
        self.assertEqual(check_email("test_123@example.com.example.co.uk"), "Invalid Email")
        self.assertEqual(check_email("test_123@example.com.example.co.uk.example"), "Invalid Email")
        self.assertEqual(check_email("test_123@example.com.example.co.uk.example.com"), "Invalid Email")
        self.assertEqual(check_email("test_123@example.com.example.co.uk.example.co
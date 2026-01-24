import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_valid_IP(self):
        self.assertEqual(check_IP("192.168.0.1"), "Valid IP address")
        self.assertEqual(check_IP("10.1.1.1"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")

    def test_invalid_IP(self):
        self.assertEqual(check_IP("192.168.0"), "Invalid IP address")
        self.assertEqual(check_IP("192.168.0.1.1"), "Invalid IP address")
        self.assertEqual(check_IP("192.168.0.1.1.1"), "Invalid IP address")

    def test_empty_IP(self):
        self.assertEqual(check_IP(""), "Invalid IP address")

    def test_IP_with_leading_zeros(self):
        self.assertEqual(check_IP("000.000.000.000"), "Valid IP address")

    def test_IP_with_leading_zeros_and_spaces(self):
        self.assertEqual(check_IP(" 000.000.000.000"), "Valid IP address")

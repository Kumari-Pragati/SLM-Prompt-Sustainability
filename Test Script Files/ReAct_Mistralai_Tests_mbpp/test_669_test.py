import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):

    def test_valid_ip(self):
        # Typical case: Valid IP address
        self.assertEqual(check_IP("192.168.1.1"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")
        self.assertEqual(check_IP("10.0.0.1"), "Valid IP address")
        self.assertEqual(check_IP("172.16.0.0"), "Valid IP address")

    def test_invalid_ip(self):
        # Edge case: Invalid IP address format
        self.assertEqual(check_IP("256.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.256.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.0.256.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.0.0.256"), "Invalid IP address")

        # Edge case: Invalid IP address range
        self.assertEqual(check_IP("128.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("172.32.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("192.256.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("203.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("204.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("223.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("224.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("240.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("255.255.255.254"), "Invalid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Invalid IP address")

    def test_empty_string(self):
        # Edge case: Empty string
        self.assertEqual(check_IP(""), "Invalid IP address")

    def test_single_dot(self):
        # Edge case: Single dot
        self.assertEqual(check_IP("."), "Invalid IP address")

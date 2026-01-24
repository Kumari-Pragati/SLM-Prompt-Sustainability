import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_valid_ip_address(self):
        self.assertEqual(check_IP("192.168.1.1"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")
        self.assertEqual(check_IP("10.0.0.1"), "Valid IP address")
        self.assertEqual(check_IP("172.16.0.0"), "Valid IP address")

    def test_invalid_ip_address(self):
        self.assertEqual(check_IP("256.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("255.255.256.255"), "Invalid IP address")
        self.assertEqual(check_IP("128.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("255.255.255.256"), "Invalid IP address")
        self.assertEqual(check_IP("255.255.255.255.1"), "Invalid IP address")
        self.assertEqual(check_IP("123.123.123.123"), "Invalid IP address")
        self.assertEqual(check_IP("a.b.c.d"), "Invalid IP address")

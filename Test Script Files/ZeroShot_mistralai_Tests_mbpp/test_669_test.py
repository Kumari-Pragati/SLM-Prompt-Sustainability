import unittest
from mbpp_669_code import search
from six69_code import check_IP

class TestCheckIP(unittest.TestCase):

    def test_valid_ip(self):
        self.assertEqual(check_IP("192.168.1.1"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")
        self.assertEqual(check_IP("10.0.0.1"), "Valid IP address")
        self.assertEqual(check_IP("172.16.0.0"), "Valid IP address")
        self.assertEqual(check_IP("203.0.113.10"), "Valid IP address")

    def test_invalid_ip(self):
        self.assertEqual(check_IP("256.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.256.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.0.256.0"), "Invalid IP address")
        self.assertEqual(check_IP("0.0.0.256"), "Invalid IP address")
        self.assertEqual(check_IP("a.b.c.d"), "Invalid IP address")
        self.assertEqual(check_IP("123.456.789.0"), "Invalid IP address")
        self.assertEqual(check_IP("123.456.789.123"), "Invalid IP address")
        self.assertEqual(check_IP("123.456.789.123.4"), "Invalid IP address")

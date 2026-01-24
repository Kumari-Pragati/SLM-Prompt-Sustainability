import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_simple_valid_ip(self):
        self.assertEqual(check_IP("192.168.1.1"), "Valid IP address")
        self.assertEqual(check_IP("10.0.0.1"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")

    def test_edge_valid_ip(self):
        self.assertEqual(check_IP("0.0.0.0"), "Valid IP address")
        self.assertEqual(check_IP("255.255.255.254"), "Valid IP address")
        self.assertEqual(check_IP("1.255.255.255"), "Valid IP address")
        self.assertEqual(check_IP("255.1.1.1"), "Valid IP address")
        self.assertEqual(check_IP("1.2.3.255"), "Valid IP address")

    def test_invalid_ip(self):
        self.assertEqual(check_IP("256.0.0.0"), "Invalid IP address")
        self.assertEqual(check_IP("1.2.3.256"), "Invalid IP address")
        self.assertEqual(check_IP("a.b.c.d"), "Invalid IP address")
        self.assertEqual(check_IP("1.2.3.a"), "Invalid IP address")
        self.assertEqual(check_IP("1..2.3.4"), "Invalid IP address")
        self.assertEqual(check_IP("1.2.3."), "Invalid IP address")
        self.assertEqual(check_IP("1.2.3.4.5"), "Invalid IP address")

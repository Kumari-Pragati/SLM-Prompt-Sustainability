import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_valid_IP(self):
        self.assertEqual(check_IP("192.168.1.1"), "Valid IP address")

    def test_invalid_IP(self):
        self.assertEqual(check_IP("192.168.1"), "Invalid IP address")

    def test_IP_with_leading_zeros(self):
        self.assertEqual(check_IP("012.168.1.1"), "Valid IP address")

    def test_IP_with_trailing_zeros(self):
        self.assertEqual(check_IP("192.168.1.01"), "Valid IP address")

    def test_IP_with_all_zeros(self):
        self.assertEqual(check_IP("0.0.0.0"), "Valid IP address")

    def test_IP_with_all_ones(self):
        self.assertEqual(check_IP("255.255.255.255"), "Valid IP address")

    def test_IP_with_non_digit_characters(self):
        self.assertEqual(check_IP("192.168.1.abc"), "Invalid IP address")

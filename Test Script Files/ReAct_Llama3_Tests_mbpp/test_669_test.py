import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(check_IP("192.168.0.1"), "Valid IP address")

    def test_invalid_ip(self):
        self.assertEqual(check_IP("192.168.0"), "Invalid IP address")

    def test_ip_with_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_ip_with_trailing_zeros(self):
        self.assertEqual(check_IP("192.168.0.012"), "Valid IP address")

    def test_ip_with_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_ip_with_non_digit_characters(self):
        self.assertEqual(check_IP("192.168.0.abc"), "Invalid IP address")

    def test_ip_with_non_digit_characters_and_leading_zeros(self):
        self.assertEqual(check_IP("012.abc.012.012"), "Invalid IP address")

    def test_ip_with_non_digit_characters_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.abc"), "Invalid IP address")

    def test_ip_with_non_digit_characters_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.abc.012.012"), "Invalid IP address")

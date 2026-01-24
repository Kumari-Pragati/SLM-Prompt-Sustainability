import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):
    def test_valid_IP(self):
        self.assertEqual(check_IP("192.168.0.1"), "Valid IP address")

    def test_invalid_IP(self):
        self.assertEqual(check_IP("192.168.0"), "Invalid IP address")

    def test_IP_with_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros_and_trailing_zeros_and_leading_zeros(self):
        self.assertEqual(check_IP("012.012.012.012"), "Valid IP address")

    def test_IP_with_leading_zeros
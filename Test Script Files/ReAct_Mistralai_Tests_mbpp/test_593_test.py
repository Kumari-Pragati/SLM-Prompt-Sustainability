import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_remove_single_zero(self):
        self.assertEqual(removezero_ip("127.0.0.1"), "127.1")

    def test_remove_multiple_zeros(self):
        self.assertEqual(removezero_ip("192.168.0.0"), "192.168.1.0")

    def test_remove_leading_zeros(self):
        self.assertEqual(removezero_ip("010.020.030.040"), "10.20.30.40")

    def test_remove_trailing_zeros(self):
        self.assertEqual(removezero_ip("123.456.789.12345"), "123.456.789.123")

    def test_remove_only_zeros(self):
        self.assertEqual(removezero_ip("0.0.0.0"), ".")

    def test_invalid_input(self):
        self.assertRaises(ValueError, removezero_ip, "invalid_ip")

    def test_empty_string(self):
        self.assertEqual(removezero_ip(""), "")

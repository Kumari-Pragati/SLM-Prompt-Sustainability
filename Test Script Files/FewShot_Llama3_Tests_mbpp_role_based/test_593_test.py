import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIp(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(removezero_ip("192.0.2.0"), "192.0.2.0")

    def test_ip_with_leading_zeros(self):
        self.assertEqual(removezero_ip("192.000.2.0"), "192.2.0.0")

    def test_ip_with_trailing_zeros(self):
        self.assertEqual(removezero_ip("192.0.2.00"), "192.0.2.0")

    def test_ip_with_multiple_zeros(self):
        self.assertEqual(removezero_ip("192.000.000.000"), "192.0.0.0")

    def test_ip_with_no_zeros(self):
        self.assertEqual(removezero_ip("192.2.3.4"), "192.2.3.4")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            removezero_ip("not an ip")

import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIp(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(removezero_ip("192.168.0.0"), "192.168.0.0")
        self.assertEqual(removezero_ip("192.168.0.1"), "192.168.0.1")
        self.assertEqual(removezero_ip("192.168.0.10"), "192.168.0.10")
        self.assertEqual(removezero_ip("192.168.0.100"), "192.168.0.100")
        self.assertEqual(removezero_ip("192.168.0.1000"), "192.168.0.1000")

    def test_ip_with_leading_zeros(self):
        self.assertEqual(removezero_ip("000.000.000.000"), "0.0.0.0")
        self.assertEqual(removezero_ip("001.001.001.001"), "1.1.1.1")
        self.assertEqual(removezero_ip("010.010.010.010"), "10.10.10.10")
        self.assertEqual(removezero_ip("100.100.100.100"), "100.100.100.100")

    def test_ip_with_trailing_zeros(self):
        self.assertEqual(removezero_ip("192.168.0.000"), "192.168.0.0")
        self.assertEqual(removezero_ip("192.168.0.001"), "192.168.0.1")
        self.assertEqual(removezero_ip("192.168.0.010"), "192.168.0.10")
        self.assertEqual(removezero_ip("192.168.0.100"), "192.168.0.100")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            removezero_ip("192.168.0")
        with self.assertRaises(ValueError):
            removezero_ip("192.168.0.100.100")
        with self.assertRaises(ValueError):
            removezero_ip("192.168.0.100.100.100")

import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(removezero_ip(''), '')

    def test_single_zero(self):
        self.assertEqual(removezero_ip('.0'), '.')

    def test_multiple_zeros(self):
        self.assertEqual(removezero_ip('.0.0.0'), '.')

    def test_single_ip(self):
        self.assertEqual(removezero_ip('127.0.0.1'), '127.0.1')

    def test_multiple_ips(self):
        self.assertEqual(removezero_ip('127.0.0.1, 192.168.0.1, 172.16.0.1'), '127.0.1, 192.168.0.1, 172.16.0.1')

    def test_invalid_ip(self):
        self.assertRaises(ValueError, removezero_ip, 'invalid.ip')

    def test_ip_with_leading_zeros(self):
        self.assertEqual(removezero_ip('0127.0.0.1'), '127.0.0.1')

    def test_ip_with_trailing_zeros(self):
        self.assertEqual(removezero_ip('127.0.0.1.'), '127.0.0.1')

    def test_ip_with_multiple_leading_and_trailing_zeros(self):
        self.assertEqual(removezero_ip('0127.0.0.1.'), '127.0.0.1')

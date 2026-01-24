import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')

    def test_multiple_consecutive_zeros(self):
        self.assertEqual(removezero_ip('192.168.000.1'), '192.168.0.1')

    def test_single_zero(self):
        self.assertEqual(removezero_ip('192.168.0.0'), '192.168.0.0')

    def test_single_octet(self):
        self.assertEqual(removezero_ip('192.168.0'), '192.168.0')

    def test_empty_string(self):
        self.assertEqual(removezero_ip(''), '')

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.256')

    def test_invalid_ip_format(self):
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.1.1')

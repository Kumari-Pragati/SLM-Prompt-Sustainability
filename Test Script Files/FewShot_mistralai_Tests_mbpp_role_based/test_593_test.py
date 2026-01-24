import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_valid_ip_with_zeroes(self):
        self.assertEqual(removezero_ip('192.168.0.0'), '192.168.0.0')
        self.assertEqual(removezero_ip('192.168.1.0'), '192.168.1.0')
        self.assertEqual(removezero_ip('192.168.1.255'), '192.168.1.255')
        self.assertEqual(removezero_ip('192.168.1.254'), '192.168.1.254')

    def test_invalid_ip_format(self):
        self.assertRaises(ValueError, removezero_ip, '192.168.1.256')
        self.assertRaises(ValueError, removezero_ip, '192.168.1.255.1')
        self.assertRaises(ValueError, removezero_ip, '192.168.1.255.255')
        self.assertRaises(ValueError, removezero_ip, '192.168.1.255.255.255')
        self.assertRaises(ValueError, removezero_ip, '192.168.1.255.255.255.255')

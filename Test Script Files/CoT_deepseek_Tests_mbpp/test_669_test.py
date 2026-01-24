import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):

    def test_valid_ip(self):
        self.assertEqual(check_IP('192.168.0.1'), 'Valid IP address')
        self.assertEqual(check_IP('10.0.0.1'), 'Valid IP address')
        self.assertEqual(check_IP('127.0.0.1'), 'Valid IP address')

    def test_invalid_ip(self):
        self.assertEqual(check_IP('256.0.0.1'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.256.1'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0.256'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0.0.1'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0.1.2'), 'Invalid IP address')
        self.assertEqual(check_IP('abc.def.ghi.jkl'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0.256'), 'Invalid IP address')
        self.assertEqual(check_IP(''), 'Invalid IP address')
        self.assertEqual(check_IP(None), 'Invalid IP address')

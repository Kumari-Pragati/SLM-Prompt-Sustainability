import unittest
from mbpp_669_code import check_IP

class TestCheckIP(unittest.TestCase):

    def test_valid_IP(self):
        self.assertEqual(check_IP('192.168.0.1'), 'Valid IP address')
        self.assertEqual(check_IP('127.0.0.1'), 'Valid IP address')
        self.assertEqual(check_IP('255.255.255.255'), 'Valid IP address')

    def test_invalid_IP(self):
        self.assertEqual(check_IP('256.0.0.1'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.0.256'), 'Invalid IP address')
        self.assertEqual(check_IP('192.168.240.1.1'), 'Invalid IP address')
        self.assertEqual(check_IP('abc.def.ghi.jkl'), 'Invalid IP address')

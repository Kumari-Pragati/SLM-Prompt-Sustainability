import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_removezero_ip(self):
        self.assertEqual(removezero_ip('192.168.0.0'), '192.168.0.0')
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')
        self.assertEqual(removezero_ip('192.168.1.0'), '192.168.1.0')
        self.assertEqual(removezero_ip('192.168.1.1'), '192.168.1.1')
        self.assertEqual(removezero_ip('192.168.0.0'), '192.168.0.0')
        self.assertEqual(removezero_ip('192.0.0.1'), '192.0.0.1')
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0.0')
        self.assertEqual(removezero_ip('123.45.67.89'), '123.45.67.89')

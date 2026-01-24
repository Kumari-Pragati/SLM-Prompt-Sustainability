import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.1.1')
        self.assertEqual(removezero_ip('123.456.789.012'), '123.456.789.12')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0')
        self.assertEqual(removezero_ip('255.255.255.255'), '255.255.255')
        self.assertEqual(removezero_ip('192.168.0.255'), '192.168.0.255')
        self.assertEqual(removezero_ip('192.168.255.255'), '192.168.255')
        self.assertEqual(removezero_ip('192.168.255'), '192.168.255')
        self.assertEqual(removezero_ip('192.168.255.0'), '192.168.255')
        self.assertEqual(removezero_ip('192.168.255.255.1'), '192.168.255.255')

    def test_invalid_input(self):
        self.assertRaises(ValueError, removezero_ip, 'invalid_ip')
        self.assertRaises(ValueError, removezero_ip, '192.168.0.-1')
        self.assertRaises(ValueError, removezero_ip, '192.168.0.256')
        self.assertRaises(ValueError, removezero_ip, '192.168.a.1')
        self.assertRaises(ValueError, removezero_ip, '192.168..1')
        self.assertRaises(ValueError, removezero_ip, '192.168.1.1.1')

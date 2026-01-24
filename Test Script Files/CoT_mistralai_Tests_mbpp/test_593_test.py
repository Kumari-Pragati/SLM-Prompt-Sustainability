import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.1.1')
        self.assertEqual(removezero_ip('123.456.789.0'), '123.456.789.9')
        self.assertEqual(removezero_ip('123.456.789.123'), '123.456.789.123')

    def test_edge_cases(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0.0')
        self.assertEqual(removezero_ip('255.255.255.255'), '255.255.255.255')
        self.assertEqual(removezero_ip('123.456.789.255'), '123.456.789.255')
        self.assertEqual(removezero_ip('123.456.789'), '123.456.789.0')
        self.assertEqual(removezero_ip('123.456'), '123.456.0.0')
        self.assertEqual(removezero_ip('123'), '123.0.0.0')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, removezero_ip, 'a.b.c.d')
        self.assertRaises(ValueError, removezero_ip, '123.456.789.a')
        self.assertRaises(ValueError, removezero_ip, '123.456.789.256')
        self.assertRaises(ValueError, removezero_ip, '123.456.789.-1')
        self.assertRaises(ValueError, removezero_ip, '123.456.789.123.456')

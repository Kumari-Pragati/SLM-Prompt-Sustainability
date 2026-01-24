import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')
        self.assertEqual(removezero_ip('10.0.0.1'), '10.0.0.1')

    def test_edge_case_single_zero(self):
        self.assertEqual(removezero_ip('192.168.0.0'), '192.168.0.0')

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(removezero_ip('192.168.0.00'), '192.168.0.0')
        self.assertEqual(removezero_ip('192.168.00.1'), '192.168.0.1')

    def test_edge_case_no_zero(self):
        self.assertEqual(removezero_ip('192.168.1.1'), '192.168.1.1')

    def test_edge_case_all_zeros(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0.0')

    def test_edge_case_single_digit(self):
        self.assertEqual(removezero_ip('1.1.1.1'), '1.1.1.1')

    def test_edge_case_large_numbers(self):
        self.assertEqual(removezero_ip('255.255.255.255'), '255.255.255.255')

    def test_edge_case_invalid_ip(self):
        with self.assertRaises(ValueError):
            removezero_ip('256.256.256.256')
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0')
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.256')
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.1.1')

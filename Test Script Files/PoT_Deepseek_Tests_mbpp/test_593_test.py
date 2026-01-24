import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')
        self.assertEqual(removezero_ip('10.0.0.1'), '10.0.0.1')

    def test_edge_case(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0.0')

    def test_boundary_case(self):
        self.assertEqual(removezero_ip('255.255.255.255'), '255.255.255.255')

    def test_corner_case(self):
        self.assertEqual(removezero_ip('192.168.00.01'), '192.168.0.1')
        self.assertEqual(removezero_ip('100.010.000.001'), '100.10.0.1')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removezero_ip(192168001)
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.256')

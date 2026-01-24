import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_simple_ip(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')
        self.assertEqual(removezero_ip('127.0.0.1'), '127.0.0.1')

    def test_edge_conditions(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '0.0.0.0')
        self.assertEqual(removezero_ip('255.255.255.255'), '255.255.255.255')

    def test_boundary_conditions(self):
        self.assertEqual(removezero_ip('1.2.3.4'), '1.2.3.4')
        self.assertEqual(removezero_ip('10.255.255.255'), '10.255.255.255')

    def test_complex_cases(self):
        self.assertEqual(removezero_ip('192.168.00.01'), '192.168.0.1')
        self.assertEqual(removezero_ip('10.020.030.040'), '10.20.30.40')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            removezero_ip(192168001)
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.256')

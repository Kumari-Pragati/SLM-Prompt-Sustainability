import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')

    def test_edge_case_with_leading_zero(self):
        self.assertEqual(removezero_ip('192.168.00.1'), '192.168.0.1')

    def test_boundary_case_with_multiple_consecutive_zeros(self):
        self.assertEqual(removezero_ip('192.168.000.1'), '192.168.0.1')

    def test_boundary_case_with_all_zeros(self):
        self.assertEqual(removezero_ip('000.000.000.000'), '0.0.0.0')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removezero_ip(192168001)

import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.1.1')

    def test_edge_case_leading_zeros(self):
        self.assertEqual(removezero_ip('000.000.000.000'), '0.0.0.0')

    def test_edge_case_trailing_zeros(self):
        self.assertEqual(removezero_ip('192.168.0.000'), '192.168.0.0')

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(removezero_ip('192.168.000.000'), '192.168.0.0')

    def test_edge_case_ip_with_leading_zeros(self):
        self.assertEqual(removezero_ip('000.000.000.000'), '0.0.0.0')

    def test_edge_case_ip_with_trailing_zeros(self):
        self.assertEqual(removezero_ip('192.168.0.000'), '192.168.0.0')

    def test_edge_case_ip_with_multiple_zeros(self):
        self.assertEqual(removezero_ip('192.168.000.000'), '192.168.0.0')

    def test_invalid_input_non_ip(self):
        with self.assertRaises(ValueError):
            removezero_ip('not an ip')

    def test_invalid_input_empty_string(self):
        with self.assertRaises(ValueError):
            removezero_ip('')

    def test_invalid_input_single_character(self):
        with self.assertRaises(ValueError):
            removezero_ip('a')

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.abc')

    def test_invalid_input_non_numeric_port(self):
        with self.assertRaises(ValueError):
            removezero_ip('192.168.0.abc:8080')

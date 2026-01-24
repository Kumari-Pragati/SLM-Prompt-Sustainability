import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIp(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(removezero_ip("192.168.0.0"), "192.168.0.0")

    def test_simple_valid_input2(self):
        self.assertEqual(removezero_ip("192.168.0.1"), "192.168.0.1")

    def test_edge_case_empty_input(self):
        self.assertEqual(removezero_ip(""), "")

    def test_edge_case_single_dot_input(self):
        self.assertEqual(removezero_ip("."), ".")

    def test_edge_case_zero_ip(self):
        self.assertEqual(removezero_ip("0.0.0.0"), "0.0.0.0")

    def test_edge_case_max_ip(self):
        self.assertEqual(removezero_ip("255.255.255.255"), "255.255.255.255")

    def test_edge_case_min_ip(self):
        self.assertEqual(removezero_ip("0.0.0.0"), "0.0.0.0")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removezero_ip("not an ip")

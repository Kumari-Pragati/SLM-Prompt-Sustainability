import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(removezero_ip("192.168.0.0"), "192.168.0.0")

    def test_edge_case_1(self):
        self.assertEqual(removezero_ip("192.168.0.00"), "192.168.0.0")

    def test_edge_case_2(self):
        self.assertEqual(removezero_ip("192.168.0.000"), "192.168.0.0")

    def test_edge_case_3(self):
        self.assertEqual(removezero_ip("192.168.0.0000"), "192.168.0.0")

    def test_edge_case_4(self):
        self.assertEqual(removezero_ip("192.168.0.0.0"), "192.168.0.0")

    def test_edge_case_5(self):
        self.assertEqual(removezero_ip("192.168.0.0.00"), "192.168.0.0")

    def test_edge_case_6(self):
        self.assertEqual(removezero_ip("192.168.0.0.000"), "192.168.0.0")

    def test_edge_case_7(self):
        self.assertEqual(removezero_ip("192.168.0.0.0000"), "192.168.0.0")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removezero_ip("192.168.0")

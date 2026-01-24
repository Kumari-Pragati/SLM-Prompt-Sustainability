import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(removezero_ip("192.168.0.0"), "192.168.0.0")

    def test_edge_case(self):
        self.assertEqual(removezero_ip("192.168.0.00"), "192.168.0.0")

    def test_edge_case2(self):
        self.assertEqual(removezero_ip("192.168.0.000"), "192.168.0.0")

    def test_edge_case3(self):
        self.assertEqual(removezero_ip("192.168.0.0.0"), "192.168.0.0")

    def test_edge_case4(self):
        self.assertEqual(removezero_ip("192.168.0.0."), "192.168.0.0")

    def test_edge_case5(self):
        self.assertEqual(removezero_ip("192.168.0.0.."), "192.168.0.0")

    def test_edge_case6(self):
        self.assertEqual(removezero_ip("192.168.0.0..."), "192.168.0.0")

    def test_edge_case7(self):
        self.assertEqual(removezero_ip("192.168.0.0...."), "192.168.0.0")

    def test_edge_case8(self):
        self.assertEqual(removezero_ip("192.168.0.0....."), "192.168.0.0")

    def test_edge_case9(self):
        self.assertEqual(removezero_ip("192.168.0.0....0"), "192.168.0.0")

    def test_edge_case10(self):
        self.assertEqual(removezero_ip("192.168.0.0....00"), "192.168.0.0")

    def test_edge_case11(self):
        self.assertEqual(removezero_ip("192.168.0.0....000"), "192.168.0.0")

    def test_edge_case12(self):
        self.assertEqual(removezero_ip("192.168.0.0....0000"), "192.168.0.0")

    def test_edge_case13(self):
        self.assertEqual(removezero_ip("192.168.0.0....00000"), "192.168.0.0")

    def test_edge_case14(self):
        self.assertEqual(removezero_ip("192.168.0.0....00000"), "192.168.0.0")

    def test_edge_case15(self):
        self.assertEqual(removezero_ip("192.168.0.0....00000"), "192.168.0.0")

    def test_edge_case16(self):
        self.assertEqual(removezero_ip("192.168.0.0....00000"), "192.168.0.0")

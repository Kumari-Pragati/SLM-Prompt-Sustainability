import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lps("abcba"), 5)

    def test_edge_case(self):
        self.assertEqual(lps("a"), 1)

    def test_boundary_case(self):
        self.assertEqual(lps(""), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lps(12345)

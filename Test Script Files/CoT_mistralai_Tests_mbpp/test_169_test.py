import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_typical_inputs(self):
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 8)
        self.assertEqual(get_pell(7), 13)
        self.assertEqual(get_pell(8), 21)
        self.assertEqual(get_pell(9), 34)

    def test_large_inputs(self):
        self.assertEqual(get_pell(100), 144)
        self.assertEqual(get_pell(1000), 1771)

    def test_edge_cases(self):
        self.assertEqual(get_pell(0), 2)
        self.assertEqual(get_pell(-1), 2)
        self.assertEqual(get_pell(-2), 2)

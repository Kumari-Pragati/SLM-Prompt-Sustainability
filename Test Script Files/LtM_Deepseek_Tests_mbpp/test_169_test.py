import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_edge_conditions(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(-1), 1)

    def test_typical_inputs(self):
        self.assertEqual(get_pell(3), 5)
        self.assertEqual(get_pell(4), 12)
        self.assertEqual(get_pell(5), 29)

    def test_large_inputs(self):
        self.assertEqual(get_pell(10), 377)
        self.assertEqual(get_pell(20), 10946)

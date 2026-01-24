import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(5), 10)
        self.assertEqual(get_pell(10), 144)

    def test_edge_cases(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(-1), None)  # Assuming the function handles negative inputs

    def test_boundary_cases(self):
        self.assertEqual(get_pell(3), 6)
        self.assertEqual(get_pell(4), 12)
        self.assertEqual(get_pell(169), 1690828853292444320)

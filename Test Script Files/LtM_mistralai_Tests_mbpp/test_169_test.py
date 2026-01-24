import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_pell(0), 2)
        self.assertEqual(get_pell(3), 7)
        self.assertEqual(get_pell(100), 297)

    def test_complex_inputs(self):
        self.assertEqual(get_pell(10), 55)
        self.assertEqual(get_pell(1000), 477639)

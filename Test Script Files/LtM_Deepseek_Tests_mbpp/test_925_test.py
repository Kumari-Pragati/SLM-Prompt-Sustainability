import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(mutiple_tuple((2, 3, 4)), 24)
        self.assertEqual(mutiple_tuple((1, 1, 1)), 1)
        self.assertEqual(mutiple_tuple((0, 1, 2)), 0)

    def test_edge_conditions(self):
        self.assertEqual(mutiple_tuple(()), 1)
        self.assertEqual(mutiple_tuple((-1,)), -1)
        self.assertEqual(mutiple_tuple((float('inf'),)), float('inf'))
        self.assertEqual(mutiple_tuple((float('-inf'),)), float('-inf'))

    def test_complex_cases(self):
        self.assertEqual(mutiple_tuple((2, 0, 3)), 0)
        self.assertEqual(mutiple_tuple((-1, -2, -3)), -6)
        self.assertEqual(mutiple_tuple((float('inf'), float('-inf'))), float('nan'))

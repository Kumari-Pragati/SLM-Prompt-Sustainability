import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(float_sort([(1.0,), (2.0,), (3.0,)]), [(3.0,), (2.0,), (1.0,)])
        self.assertEqual(float_sort([(0.0,), (1.0,), (2.0,)]), [(2.0,), (1.0,), (0.0,)])
        self.assertEqual(float_sort([(1.1,), (1.0,), (1.2,)]), [(1.2,), (1.1,), (1.0,)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(float_sort([]), [])
        self.assertEqual(float_sort([(float('inf'),)]), [(float('inf'),)])
        self.assertEqual(float_sort([(float('-inf'),)]), [(float('-inf'),)])

    def test_complex_input(self):
        self.assertEqual(float_sort([(1.0, 'a'), (2.0, 'b'), (3.0, 'a')]), [(3.0, 'a'), (2.0, 'b'), (1.0, 'a')])
        self.assertEqual(float_sort([(1.0, 'a'), (2.0, 'b'), (1.0, 'a')]), [(2.0, 'b'), (1.0, 'a'), (1.0, 'a')])

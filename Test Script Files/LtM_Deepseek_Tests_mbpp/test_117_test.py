import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(list_to_float([('1', '2'), ('3', '4')]), '[(1.0, 2.0), (3.0, 4.0)]')

    def test_edge_conditions(self):
        self.assertEqual(list_to_float([]), '[]')
        self.assertEqual(list_to_float([('a', 'b')]), '[(a, b)]')

    def test_complex_cases(self):
        self.assertEqual(list_to_float([('1', 'a'), ('b', '2')]), '[(1.0, a), (b, 2.0)]')
        self.assertEqual(list_to_float([('1', '2'), ('3', 'a')]), '[(1.0, 2.0), (3.0, a)]')
        self.assertEqual(list_to_float([('a', 'b'), ('c', 'd')]), '[(a, b), (c, d)]')

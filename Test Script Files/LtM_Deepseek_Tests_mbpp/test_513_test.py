import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(add_str((1, 2), 3), [(1, 3), (2, 3)])
        self.assertEqual(add_str(('a', 'b'), 'c'), [('a', 'c'), ('b', 'c')])

    def test_edge_conditions(self):
        self.assertEqual(add_str((), 'test'), [])
        self.assertEqual(add_str((1, 2, 3), ''), [('', ''), ('', ''), ('', '')])

    def test_complex_cases(self):
        self.assertEqual(add_str((1, 2, 3), None), [(1, None), (2, None), (3, None)])
        self.assertEqual(add_str(('a', 'b', 'c'), 'test'), [('a', 'test'), ('b', 'test'), ('c', 'test')])

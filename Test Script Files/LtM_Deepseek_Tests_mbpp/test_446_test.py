import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)
        self.assertEqual(count_Occurrence(('1', '2', '3'), ['1', '2', '3']), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_Occurrence((), ['a', 'b', 'c']), 0)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), []), 0)
        self.assertEqual(count_Occurrence((), ()), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a']), 1)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['b']), 1)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['c']), 1)

    def test_complex_cases(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c', 'a'), ['a']), 2)
        self.assertEqual(count_Occurrence(('1', '2', '3', '1'), ['1']), 2)
        self.assertEqual(count_Occurrence(('a', 'b', 'c', 'b'), ['b']), 2)

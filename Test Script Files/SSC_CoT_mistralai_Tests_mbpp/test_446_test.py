import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4]), 3)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'd']), 2)

    def test_edge_input(self):
        self.assertEqual(count_Occurrence((), []), 0)
        self.assertEqual(count_Occurrence((1,), []), 0)
        self.assertEqual(count_Occurrence([1], ()), 0)
        self.assertEqual(count_Occurrence([1], (1,)), 1)
        self.assertEqual(count_Occurrence((1,), [1, 2, 1]), 2)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'a']), 2)

    def test_boundary_input(self):
        self.assertEqual(count_Occurrence((-10, 0, 10), [0]), 1)
        self.assertEqual(count_Occurrence(('z',), ['a', 'b', 'z']), 1)
        self.assertEqual(count_Occurrence((0,), [0.0]), 1)
        self.assertEqual(count_Occurrence(('0',), ['0']), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_Occurrence, (1, 'a'), [1, 2])
        self.assertRaises(TypeError, count_Occurrence, [1, 2], (1, 'a'))

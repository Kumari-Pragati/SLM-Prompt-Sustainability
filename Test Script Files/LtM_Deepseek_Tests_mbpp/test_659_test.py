import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Repeat([1, 2, 2, 3]), [2])
        self.assertEqual(Repeat(['a', 'b', 'b', 'c']), ['b'])
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_edge_conditions(self):
        self.assertEqual(Repeat([]), [])
        self.assertEqual(Repeat([1]), [])
        self.assertEqual(Repeat(['a']), [])

    def test_complex_cases(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(Repeat(['a', 'b', 'b', 'c', 'c', 'c']), ['b', 'c'])
        self.assertEqual(Repeat([1, 1, 1, 1, 1, 1]), [1])
        self.assertEqual(Repeat(['a', 'a', 'a', 'a', 'a', 'a']), ['a'])

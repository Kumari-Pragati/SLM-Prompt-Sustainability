import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair(['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [1], [2]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_samepair([1]*1000, [1]*1000, [1]*1000), 1000)
        self.assertEqual(count_samepair([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 5)

    def test_complex_cases(self):
        self.assertEqual(count_samepair([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]), 5)
        self.assertEqual(count_samepair(['a', 'b', 'c', 'd', 'e'], ['e', 'd', 'c', 'b', 'a'], ['a', 'b', 'c', 'd', 'e']), 5)

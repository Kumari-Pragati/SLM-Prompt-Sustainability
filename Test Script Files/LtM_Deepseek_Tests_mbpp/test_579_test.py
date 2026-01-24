import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1, 4))
        self.assertEqual(find_dissimilar(('a', 'b', 'c'), ('b', 'c', 'd')), ('a', 'd'))

    def test_empty_inputs(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_edge_conditions(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())
        self.assertEqual(find_dissimilar((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(find_dissimilar((1, 2, 3), ()), (1, 2, 3))

    def test_complex_cases(self):
        self.assertEqual(find_dissimilar((1, 2, 2, 3), (2, 3, 3, 4)), (1, 4))
        self.assertEqual(find_dissimilar(('a', 'a', 'b', 'c'), ('b', 'c', 'c', 'd')), ('a', 'd'))

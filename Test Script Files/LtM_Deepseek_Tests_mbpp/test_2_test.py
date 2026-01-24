import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
        self.assertEqual(similar_elements(('a', 'b', 'c'), ('b', 'c', 'd')), ('b', 'c'))

    def test_edge_conditions(self):
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((), (1, 2, 3)), ())
        self.assertEqual(similar_elements((1, 2, 3), ()), ())

    def test_complex_cases(self):
        self.assertEqual(similar_elements((1, 2, 2, 3), (2, 2, 3, 4)), (2, 2, 3))
        self.assertEqual(similar_elements(('a', 'a', 'b', 'c'), ('a', 'b', 'c', 'c')), ('a', 'b', 'c'))

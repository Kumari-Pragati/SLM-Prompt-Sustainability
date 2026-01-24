import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements_typical(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (3, 4, 5, 6)), (3, 4))
        self.assertEqual(similar_elements(('a', 'b', 'c', 'd'), ('d', 'e', 'f', 'c')), ('d', 'c'))

    def test_similar_elements_edge_cases(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), ())
        self.assertEqual(similar_elements((1, 2, 3), ()), ())
        self.assertEqual(similar_elements((), (1, 2, 3)), ())
        self.assertEqual(similar_elements((1, 2, 3), (1, 1, 2, 3)), (2))
        self.assertEqual(similar_elements(('a', 'b', 'c'), ('a', 'b', 'd')), ())

    def test_similar_elements_invalid_inputs(self):
        self.assertRaises(TypeError, similar_elements, 1, 2)
        self.assertRaises(TypeError, similar_elements, ('a',), 1)
        self.assertRaises(TypeError, similar_elements, 1, ('a', 'b'))

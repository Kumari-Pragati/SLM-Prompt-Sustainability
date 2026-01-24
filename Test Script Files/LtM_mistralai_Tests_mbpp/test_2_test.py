import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 4, 5)), (3,))
        self.assertEqual(similar_elements(('a', 'b', 'c'), ('c', 'd', 'e')), ('c',))

    def test_edge_cases(self):
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((1,), (1,)), (1,))
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3, 4)), (1, 2, 3))
        self.assertEqual(similar_elements(('a', 'b', 'c'), ('a', 'b', 'd')), ())

    def test_complex(self):
        self.assertEqual(similar_elements((1, 2, 3, 1), (3, 4, 5, 3)), (3,))
        self.assertEqual(similar_elements(('a', 'b', 'c', 'a'), ('c', 'd', 'a')), ('c', 'a'))

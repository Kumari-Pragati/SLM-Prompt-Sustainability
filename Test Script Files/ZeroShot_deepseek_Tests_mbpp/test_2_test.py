import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
        self.assertEqual(similar_elements(('a', 'b', 'c'), ('b', 'c', 'd')), ('b', 'c'))
        self.assertEqual(similar_elements((1, 2, 2, 3, 3), (2, 2, 3, 3, 4)), (2, 3))
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((1,), (1,)), (1,))

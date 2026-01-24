import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):
    def test_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((1, 2, 3), ()), ())
        self.assertEqual(similar_elements((1, 2, 3, 4), (1, 2, 3, 4, 5)), (1, 2, 3, 4))

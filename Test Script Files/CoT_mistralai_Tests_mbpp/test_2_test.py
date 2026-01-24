import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements_same_tuples(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (1, 2, 3, 4)), (1, 2, 3))
        self.assertEqual(similar_elements((5, 6, 7, 8), (5, 6, 7, 8)), (5, 6, 7))

    def test_similar_elements_different_order(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 2, 1)), (1, 2, 3))
        self.assertEqual(similar_elements((4, 5, 6), (6, 5, 4)), (4, 5, 6))

    def test_similar_elements_single_element(self):
        self.assertEqual(similar_elements((1,), (1,)), (1,))
        self.assertEqual(similar_elements((2,), (2,)), (2,))

    def test_similar_elements_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_similar_elements_different_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())
        self.assertEqual(similar_elements((7, 8, 9), (1, 2, 3)), ())

    def test_similar_elements_invalid_input(self):
        self.assertRaises(TypeError, similar_elements, 1, 2)
        self.assertRaises(TypeError, similar_elements, (1, 'a'), (1, 2))

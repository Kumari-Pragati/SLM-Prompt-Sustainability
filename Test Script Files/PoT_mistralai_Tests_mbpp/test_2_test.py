import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements_typical(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (3, 4, 5, 6)), (3, 4))
        self.assertEqual(similar_elements(('a', 'b', 'c', 'd'), ('d', 'e', 'c', 'a')), ('d', 'c', 'a'))
        self.assertEqual(similar_elements((1.0, 2.0, 3.0, 4.0), (3.0, 4.0, 5.0, 6.0)), (3.0, 4.0))

    def test_similar_elements_empty(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_similar_elements_single_element(self):
        self.assertEqual(similar_elements((1,), (1, 2, 3)), (1,))
        self.assertEqual(similar_elements((), (1,)), ())

    def test_similar_elements_different_types(self):
        self.assertEqual(similar_elements(('a', 'b', 'c'), (1, 2, 3)), ())
        self.assertEqual(similar_elements((1, 2, 3), ('a', 'b', 'c')), ())

    def test_similar_elements_none(self):
        self.assertRaises(TypeError, similar_elements, (None,), (None,))
        self.assertRaises(TypeError, similar_elements, (1,), (None,))

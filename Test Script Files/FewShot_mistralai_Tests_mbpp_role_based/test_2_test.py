import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):
    def test_similar_elements_positive(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (3, 4, 5, 6)), (3, 4))
        self.assertEqual(similar_elements(('a', 'b', 'c', 'd'), ('d', 'e', 'c', 'a')), ('c', 'd'))
        self.assertEqual(similar_elements((1.0, 2.0, 3.0, 4.0), (3, 4, 5, 6)), ())

    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), (1, 2, 3)), ())
        self.assertEqual(similar_elements((1, 2, 3), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(similar_elements((1,), (1, 2, 3)), (1,))
        self.assertEqual(similar_elements((1, 2, 3), (1,)), (1,))

    def test_single_element_in_both_tuples(self):
        self.assertEqual(similar_elements((1, 2, 1), (1, 2, 3)), (1,))

    def test_different_data_types(self):
        self.assertEqual(similar_elements((1, 2, 3), ('a', 'b', 'c')), ())
        self.assertEqual(similar_elements(('a', 'b', 'c'), (1, 2, 3)), ())

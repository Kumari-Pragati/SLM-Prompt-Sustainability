import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 4, 5)), (3,))

    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_all_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_no_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_duplicate_elements(self):
        self.assertEqual(similar_elements((1, 2, 2), (2, 2, 3)), (2, 2))

    def test_large_tuples(self):
        self.assertEqual(similar_elements(
            tuple(range(1, 10001)), tuple(range(5000, 15001))), 
            tuple(range(5000, 10001)))

import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1,))

    def test_edge_case_empty(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_edge_case_single(self):
        self.assertEqual(find_dissimilar((1,), ()), (1,))

    def test_edge_case_empty_again(self):
        self.assertEqual(find_dissimilar((), (1,)), (1,))

    def test_edge_case_single_again(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())

    def test_edge_case_duplicates(self):
        self.assertEqual(find_dissimilar((1, 1, 2), (1, 2, 2)), (1,))

    def test_edge_case_duplicates_again(self):
        self.assertEqual(find_dissimilar((1, 2, 2), (1, 2, 2)), ())

    def test_edge_case_duplicates_all(self):
        self.assertEqual(find_dissimilar((1, 1, 1, 2, 2, 2), (1, 1, 1, 2, 2, 2)), ())

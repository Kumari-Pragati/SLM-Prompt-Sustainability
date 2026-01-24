import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 4)), (3, 4))
        self.assertEqual(find_dissimilar((4, 3, 2), (1, 2, 3)), (4, 1))
        self.assertEqual(find_dissimilar((), ()), ())

    def test_edge_and_boundary(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())
        self.assertEqual(find_dissimilar((1,), (1, 1)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 5)), (5,))

    def test_complex(self):
        self.assertEqual(find_dissimilar((1, 1, 2, 2), (1, 2, 3, 4)), (3, 4, 1, 2))
        self.assertEqual(find_dissimilar((1, 1, 2, 2), (1, 2, 2, 3)), (3,))
        self.assertEqual(find_dissimilar((1, 1, 2, 2), (1, 2, 2, 2)), ())

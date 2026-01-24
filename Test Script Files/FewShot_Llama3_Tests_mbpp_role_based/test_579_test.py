import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(find_dissimilar((1,), ()), (1,))
        self.assertEqual(find_dissimilar((), (2,)), (2,))
        self.assertEqual(find_dissimilar((1,), (2,)), (1, 2))

    def test_multiple_element_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1, 4))
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())
        self.assertEqual(find_dissimilar((1, 2, 3, 4), (2, 3, 4, 5)), (1, 5))

    def test_tuple_with_duplicates(self):
        self.assertEqual(find_dissimilar((1, 1, 2), (1, 2, 2)), (1, 2))

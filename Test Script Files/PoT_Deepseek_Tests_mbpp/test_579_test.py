import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1, 4))

    def test_empty_tuples(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())

    def test_identical_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())

    def test_duplicate_elements(self):
        self.assertEqual(find_dissimilar((1, 2, 2, 3), (2, 2, 3, 4)), (1, 4))

    def test_unequal_length_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3)), (1,))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 10001))
        self.assertEqual(find_dissimilar(large_tuple, large_tuple), ())

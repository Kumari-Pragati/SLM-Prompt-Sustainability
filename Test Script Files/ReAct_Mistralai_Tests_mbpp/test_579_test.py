import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(find_dissimilar((1,), (1,)), ())
        self.assertEqual(find_dissimilar((1,), (2,)), (1, 2))

    def test_identical_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())

    def test_dissimilar_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_mixed_types(self):
        self.assertEqual(find_dissimilar((1, 'a'), (1, 'b')), ('a', 'b'))
        self.assertEqual(find_dissimilar((1, 'a'), (1, 2)), ('a',))

    def test_duplicate_elements(self):
        self.assertEqual(find_dissimilar((1, 1, 2), (1, 2, 2)), (1, 2))

    def test_large_tuples(self):
        tup1 = tuple(range(10))
        tup2 = tuple(reversed(range(10)))
        self.assertEqual(find_dissimilar(tup1, tup2), tuple(reversed(range(1, 11))))

import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1, 4))

    def test_empty_tuples(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_one_empty_tuple(self):
        self.assertEqual(find_dissimilar((1, 2, 3), ()), (1, 2, 3))
        self.assertEqual(find_dissimilar((), (1, 2, 3)), (1, 2, 3))

    def test_duplicate_elements(self):
        self.assertEqual(find_dissimilar((1, 2, 2, 3), (2, 3, 3, 4)), (1, 4))

    def test_same_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_dissimilar(123, (1, 2, 3))
        with self.assertRaises(TypeError):
            find_dissimilar((1, 2, 3), 123)

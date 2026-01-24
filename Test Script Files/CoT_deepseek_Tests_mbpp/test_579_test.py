import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (2, 3, 4)), (1, 4))

    def test_empty_tuples(self):
        self.assertEqual(find_dissimilar((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(find_dissimilar((1,), (2,)), (1, 2))

    def test_duplicate_elements(self):
        self.assertEqual(find_dissimilar((1, 2, 2), (2, 3, 3)), (1,))

    def test_same_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (1, 2, 3)), ())

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 10001))
        self.assertEqual(find_dissimilar(large_tuple, large_tuple), ())

    def test_unequal_length_tuples(self):
        self.assertEqual(find_dissimilar((1, 2, 3), (4, 5)), (1, 2, 3, 4, 5))

    def test_non_tuple_inputs(self):
        with self.assertRaises(TypeError):
            find_dissimilar([1, 2, 3], (2, 3, 4))

        with self.assertRaises(TypeError):
            find_dissimilar((1, 2, 3), [2, 3, 4])

        with self.assertRaises(TypeError):
            find_dissimilar([1, 2, 3], [2, 3, 4])

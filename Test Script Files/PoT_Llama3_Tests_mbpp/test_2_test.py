import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))

    def test_empty_input(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_single_input(self):
        self.assertEqual(similar_elements((1, 2, 3), ()), ())

    def test_equal_input(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_disjoint_input(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_subset_input(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2)), (1, 2))

    def test_superset_input(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3, 4)), (1, 2, 3))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            similar_elements([1, 2, 3], (2, 3, 4))

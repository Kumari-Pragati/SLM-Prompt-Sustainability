import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_sets(self):
        self.assertFalse(check_subset((), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3), ()))

    def test_single_element_sets(self):
        self.assertFalse(check_subset((1,), (2, 3)))
        self.assertTrue(check_subset((2, 3), (1,)))

    def test_equal_sets(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_subset_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3, 4)))

    def test_superset_case(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))

    def test_disjoint_sets(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6)))
        self.assertFalse(check_subset((4, 5, 6), (1, 2, 3)))

    def test_duplicates_case(self):
        self.assertTrue(check_subset((1, 1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3), (1, 1, 2, 3)))

    def test_negative_case_1(self):
        with self.assertRaises(TypeError):
            check_subset(1, (1, 2, 3))

    def test_negative_case_2(self.assertRaises(TypeError):
        check_subset([1, 2, 3], 1)

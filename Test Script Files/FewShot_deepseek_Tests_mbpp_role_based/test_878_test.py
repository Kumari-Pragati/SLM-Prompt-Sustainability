import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_typical_use_case(self):
        K = (1, 2, 3)
        test_tuple = (1, 2)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_edge_condition(self):
        K = ()
        test_tuple = ()
        self.assertTrue(check_tuples(test_tuple, K))

    def test_boundary_condition(self):
        K = (1,)
        test_tuple = (1,)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_typical_use_case_with_duplicates(self):
        K = (1, 2, 3)
        test_tuple = (2, 3, 1)
        self.assertTrue(check_tuples(test_tuple, K))

    def test_typical_use_case_with_extra_elements(self):
        K = (1, 2, 3)
        test_tuple = (2, 3, 1, 4)
        self.assertFalse(check_tuples(test_tuple, K))

    def test_typical_use_case_with_missing_elements(self):
        K = (1, 2, 3)
        test_tuple = (2, 3)
        self.assertFalse(check_tuples(test_tuple, K))

    def test_invalid_input(self):
        K = (1, 2, 3)
        test_tuple = "1, 2, 3"
        with self.assertRaises(TypeError):
            check_tuples(test_tuple, K)

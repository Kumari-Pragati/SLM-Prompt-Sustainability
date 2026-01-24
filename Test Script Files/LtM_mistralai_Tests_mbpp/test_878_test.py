import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))
        self.assertTrue(check_tuples((4, 5, 6), [4, 5, 6]))

    def test_edge_cases(self):
        self.assertFalse(check_tuples((1, 2, 3), []))
        self.assertFalse(check_tuples([], [1, 2, 3]))
        self.assertFalse(check_tuples((1, 2, 3), [1, 2]))
        self.assertFalse(check_tuples((1, 2, 3), [3, 2, 1]))
        self.assertFalse(check_tuples((1, 2, 3), [4, 5, 6, 7]))

    def test_complex_cases(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3, 4]))
        self.assertTrue(check_tuples((1, 2, 3), [3, 2, 1, 4]))
        self.assertFalse(check_tuples((1, 2, 3), [4, 3, 2, 1]))
        self.assertFalse(check_tuples((1, 2, 3), [4, 5, 6, 1, 2, 3]))

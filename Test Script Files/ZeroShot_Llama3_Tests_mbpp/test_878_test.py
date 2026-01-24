import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_check_tuples(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))
        self.assertFalse(check_tuples((1, 2, 3), [1, 2]))
        self.assertFalse(check_tuples((1, 2, 3), [1, 3]))
        self.assertFalse(check_tuples((1, 2, 3), [2, 3]))
        self.assertFalse(check_tuples((1, 2, 3), [4, 5, 6]))
        self.assertFalse(check_tuples((1, 2, 3), [1, 2, 3, 4]))

    def test_check_tuples_empty(self):
        self.assertFalse(check_tuples((), [1, 2, 3]))
        self.assertFalse(check_tuples((1, 2, 3), []))

    def test_check_tuples_single_element(self):
        self.assertTrue(check_tuples((1,), [1]))
        self.assertFalse(check_tuples((1,), [2]))

    def test_check_tuples_single_element_empty(self):
        self.assertFalse(check_tuples((), []))

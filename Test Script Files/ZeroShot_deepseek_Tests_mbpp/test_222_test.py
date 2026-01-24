import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_same_type(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type((True, False, True)))

    def test_different_type(self):
        self.assertFalse(check_type((1, '2', 3)))
        self.assertFalse(check_type(('a', 2, 'c')))
        self.assertFalse(check_type((True, 'False', True)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))

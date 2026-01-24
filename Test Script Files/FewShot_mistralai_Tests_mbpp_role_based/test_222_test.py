import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_valid_tuple_of_same_type(self):
        self.assertTrue(check_type((1, 1, 1)))
        self.assertTrue(check_type((3.14, 3.14, 3.14)))
        self.assertTrue(check_type(('a', 'a', 'a')))

    def test_valid_tuple_of_different_types(self):
        self.assertFalse(check_type((1, 3.14, 'a')))
        self.assertFalse(check_type((3.14, 1, 'a')))
        self.assertFalse(check_type(('a', 3.14, 1)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))
        self.assertTrue(check_type((3.14,)))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_type, 1)
        self.assertRaises(TypeError, check_type, 'a')
        self.assertRaises(TypeError, check_type, (1, 'a'))

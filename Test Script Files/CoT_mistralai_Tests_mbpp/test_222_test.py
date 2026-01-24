import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_valid_tuple(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type([1, 2, 3]))

    def test_mixed_types_tuple(self):
        self.assertFalse(check_type((1, 'a', 3)))
        self.assertFalse(check_type(('a', 1, 'c')))
        self.assertFalse(check_type([1, 'b', 3]))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))
        self.assertTrue(check_type([1]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_type, 1)
        self.assertRaises(TypeError, check_type, 'str')
        self.assertRaises(TypeError, check_type, [1, 2, 'str'])

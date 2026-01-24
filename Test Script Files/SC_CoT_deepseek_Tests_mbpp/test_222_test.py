import unittest

from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type((1.1, 2.2, 3.3)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))

    def test_different_types(self):
        self.assertFalse(check_type((1, 'a')))
        self.assertFalse(check_type((1, 2, 'a')))

    def test_mixed_numeric_types(self):
        self.assertFalse(check_type((1, 2.2, 3)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_type(1)
        with self.assertRaises(TypeError):
            check_type('a')
        with self.assertRaises(TypeError):
            check_type(None)

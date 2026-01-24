import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_same_type_elements(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type((True, False, True)))

    def test_different_type_elements(self):
        self.assertFalse(check_type((1, 'a', True)))
        self.assertFalse(check_type((1, 2.0, True)))
        self.assertFalse(check_type((1, 'a')))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))
        self.assertTrue(check_type((True,)))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            check_type(1)
        with self.assertRaises(TypeError):
            check_type('a')
        with self.assertRaises(TypeError):
            check_type(True)

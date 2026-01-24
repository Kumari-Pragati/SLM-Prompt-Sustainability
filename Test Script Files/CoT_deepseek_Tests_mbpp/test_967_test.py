import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check('aeiou'), 'accepted')
        self.assertEqual(check('AEIOU'), 'accepted')
        self.assertEqual(check('AEIOUaeiou'), 'accepted')

    def test_boundary_conditions(self):
        self.assertEqual(check(''), 'not accepted')
        self.assertEqual(check('bcdfghjklmnpqrstvwxyz'), 'not accepted')
        self.assertEqual(check('AEIOUaeiou'*10000), 'accepted')

    def test_edge_cases(self):
        self.assertEqual(check('AEIOUaeiouAEIOUaeiou'), 'accepted')
        self.assertEqual(check('AEIOUaeiouAEIOUaeiouAEIOUaeiou'), 'accepted')
        self.assertEqual(check('AEIOUaeiouAEIOUaeiouAEIOUaeiouAEIOUaeiou'), 'not accepted')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check(12345)
        with self.assertRaises(TypeError):
            check(['a', 'e', 'i', 'o', 'u'])
        with self.assertRaises(TypeError):
            check({'a', 'e', 'i', 'o', 'u'})
        with self.assertRaises(TypeError):
            check(None)

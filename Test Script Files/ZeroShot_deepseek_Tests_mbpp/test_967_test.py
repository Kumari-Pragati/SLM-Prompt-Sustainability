import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_accepted(self):
        self.assertEqual(check('aeiou'), 'accepted')
        self.assertEqual(check('AEIOU'), 'accepted')
        self.assertEqual(check('AEIOUaeiou'), 'accepted')
        self.assertEqual(check('AEIOUaeiouy'), 'accepted')
        self.assertEqual(check('AEIOUaeiouyAEIOU'), 'accepted')

    def test_not_accepted(self):
        self.assertEqual(check('bcdfghjklmnpqrstvwxyz'), 'not accepted')
        self.assertEqual(check('AEIOUaeiouyBCDFGHJKLMNPQRSTVWXYZ'), 'not accepted')
        self.assertEqual(check(''), 'not accepted')
        self.assertEqual(check('a'), 'not accepted')
        self.assertEqual(check('aei'), 'not accepted')

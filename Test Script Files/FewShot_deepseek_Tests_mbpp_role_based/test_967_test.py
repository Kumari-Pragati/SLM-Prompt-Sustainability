import unittest
from mbpp_967_code import check

class TestCheck(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check('aeiou'), 'accepted')

    def test_boundary_case(self):
        self.assertEqual(check('aeiouy'), 'accepted')

    def test_edge_case(self):
        self.assertEqual(check('aeiouy'), 'accepted')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check(12345)

import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')
        self.assertEqual(check_Equality('12321'), 'Equal')

    def test_edge_cases(self):
        self.assertEqual(check_Equality('a'), 'Equal')
        self.assertEqual(check_Equality(''), 'Equal')

    def test_boundary_cases(self):
        self.assertEqual(check_Equality('ab'), 'Not Equal')
        self.assertEqual(check_Equality('123'), 'Not Equal')

    def test_corner_cases(self):
        self.assertEqual(check_Equality(' '), 'Not Equal')
        self.assertEqual(check_Equality('!@#$%^&*('), 'Not Equal')

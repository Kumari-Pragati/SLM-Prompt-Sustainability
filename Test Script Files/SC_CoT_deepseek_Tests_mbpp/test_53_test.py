import unittest

from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')

    def test_edge_case(self):
        self.assertEqual(check_Equality('a'), 'Equal')

    def test_boundary_case(self):
        self.assertEqual(check_Equality(''), 'Equal')

    def test_special_case(self):
        self.assertEqual(check_Equality('123321'), 'Equal')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Equality(12345)

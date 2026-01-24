import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')

    def test_single_character(self):
        self.assertEqual(check_Equality('a'), 'Equal')

    def test_empty_string(self):
        self.assertEqual(check_Equality(''), 'Equal')

    def test_different_characters(self):
        self.assertEqual(check_Equality('abca'), 'Not Equal')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            check_Equality(None)

import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')
        self.assertEqual(check_Equality('12321'), 'Equal')
        self.assertEqual(check_Equality('a'), 'Equal')
        self.assertEqual(check_Equality(''), 'Equal')

    def test_edge_cases(self):
        self.assertEqual(check_Equality('abca'), 'Not Equal')
        self.assertEqual(check_Equality('1234'), 'Not Equal')
        self.assertEqual(check_Equality('a'*10000 + 'b'), 'Not Equal')

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            check_Equality(12345)
        with self.assertRaises(TypeError):
            check_Equality(['a', 'b', 'c', 'd'])

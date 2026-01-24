import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_strings(self):
        self.assertEqual(check_str('A123_'), 'Valid')
        self.assertEqual(check_str('a123_'), 'Valid')
        self.assertEqual(check_str('U987_'), 'Valid')
        self.assertEqual(check_str('u987_'), 'Valid')

    def test_invalid_strings(self):
        self.assertEqual(check_str('123_'), 'Invalid')
        self.assertEqual(check_str('a1234'), 'Invalid')
        self.assertEqual(check_str('A'), 'Invalid')
        self.assertEqual(check_str(''), 'Invalid')

    def test_edge_cases(self):
        self.assertEqual(check_str(' '), 'Invalid')
        self.assertEqual(check_str('a'*201), 'Invalid')
        self.assertEqual(check_str('A'*201), 'Invalid')
        self.assertEqual(check_str('U'*201), 'Invalid')
        self.assertEqual(check_str('u'*201), 'Invalid')

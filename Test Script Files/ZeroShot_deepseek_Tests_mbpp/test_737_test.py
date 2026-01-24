import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_strings(self):
        self.assertEqual(check_str('A123_a'), 'Valid')
        self.assertEqual(check_str('a123_a'), 'Valid')
        self.assertEqual(check_str('E456_e'), 'Valid')
        self.assertEqual(check_str('e456_e'), 'Valid')
        self.assertEqual(check_str('U789_u'), 'Valid')
        self.assertEqual(check_str('u789_u'), 'Valid')

    def test_invalid_strings(self):
        self.assertEqual(check_str('123_a'), 'Invalid')
        self.assertEqual(check_str('A1234'), 'Invalid')
        self.assertEqual(check_str('a1234'), 'Invalid')
        self.assertEqual(check_str('E4567'), 'Invalid')
        self.assertEqual(check_str('e4567'), 'Invalid')
        self.assertEqual(check_str('U7890'), 'Invalid')
        self.assertEqual(check_str('u7890'), 'Invalid')
        self.assertEqual(check_str(''), 'Invalid')

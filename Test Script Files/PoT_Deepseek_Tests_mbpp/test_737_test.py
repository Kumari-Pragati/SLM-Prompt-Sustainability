import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(check_str('a123_abc'), 'Valid')
        self.assertEqual(check_str('A987_XYZ'), 'Valid')
        self.assertEqual(check_str('e456_def'), 'Valid')
        self.assertEqual(check_str('i789_jkl'), 'Valid')
        self.assertEqual(check_str('o012_mno'), 'Valid')
        self.assertEqual(check_str('u345_pqr'), 'Valid')

    def test_edge_cases(self):
        self.assertEqual(check_str(''), 'Invalid')
        self.assertEqual(check_str('123_abc'), 'Invalid')
        self.assertEqual(check_str('A'), 'Invalid')
        self.assertEqual(check_str('a'), 'Invalid')
        self.assertEqual(check_str('I'), 'Invalid')
        self.assertEqual(check_str('i'), 'Invalid')

    def test_boundary_cases(self):
        self.assertEqual(check_str('_'*256), 'Invalid')
        self.assertEqual(check_str('_'*257), 'Invalid')
        self.assertEqual(check_str('_'*255), 'Valid')

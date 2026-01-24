import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(check_str('a123_abc'), 'Valid')
        self.assertEqual(check_str('A_123abc'), 'Valid')
        self.assertEqual(check_str('e_special'), 'Valid')
        self.assertEqual(check_str('i_start'), 'Valid')
        self.assertEqual(check_str('o_middle'), 'Valid')
        self.assertEqual(check_str('u_end'), 'Valid')
        
    def test_edge_cases(self):
        self.assertEqual(check_str(''), 'Invalid')
        self.assertEqual(check_str('123_abc'), 'Invalid')
        self.assertEqual(check_str('A'), 'Invalid')
        self.assertEqual(check_str('b_start'), 'Invalid')
        self.assertEqual(check_str('i_special'), 'Invalid')
        self.assertEqual(check_str('o_middle'), 'Invalid')
        self.assertEqual(check_str('u_end'), 'Invalid')
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_str(12345)
        with self.assertRaises(TypeError):
            check_str(['a123_abc'])
        with self.assertRaises(TypeError):
            check_str({'a123_abc': 'Valid'})

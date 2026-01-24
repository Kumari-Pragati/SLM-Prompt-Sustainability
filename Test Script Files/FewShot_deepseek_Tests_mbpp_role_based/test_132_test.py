import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_character_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_numeric_tuple(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')

    def test_mixed_type_tuple(self):
        self.assertEqual(tup_string(('a', 1, True)), 'a1True')

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            tup_string(123)

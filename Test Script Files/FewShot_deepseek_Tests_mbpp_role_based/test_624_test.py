import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(is_upper('hello'), 'HELLO')

    def test_empty_string(self):
        self.assertEqual(is_upper(''), '')

    def test_all_lower_case(self):
        self.assertEqual(is_upper('lower'), 'LOWER')

    def test_all_upper_case(self):
        self.assertEqual(is_upper('UPPER'), 'UPPER')

    def test_mixed_case(self):
        self.assertEqual(is_upper('MiXeD'), 'MIXED')

    def test_numeric_string(self):
        self.assertEqual(is_upper('12345'), '12345')

    def test_special_characters(self):
        self.assertEqual(is_upper('!@#$%^&*()'), '!@#$%^&*()')

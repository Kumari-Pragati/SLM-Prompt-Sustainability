import unittest
from mbpp_624_code import str
from six.moves.string_types import StringIO

class TestIsUpper(unittest.TestCase):

    def test_is_upper_string(self):
        self.assertTrue(is_upper('HELLO'))

    def test_is_upper_empty_string(self):
        self.assertTrue(is_upper(''))

    def test_is_upper_single_char(self):
        self.assertTrue(is_upper('A'))

    def test_is_upper_mixed_case(self):
        self.assertFalse(is_upper('Hello'))

    def test_is_upper_whitespace(self):
        self.assertTrue(is_upper('   '))

    def test_is_upper_unicode(self):
        buffer = StringIO()
        is_upper(u'\u0048\u0065\u006c\u006c\u006f')
        self.assertEqual(buffer.getvalue(), 'HELLO')
        self.assertTrue(is_upper(buffer.getvalue()))

    def test_is_upper_none(self):
        self.assertRaises(TypeError, is_upper, None)

    def test_is_upper_list(self):
        self.assertRaises(TypeError, is_upper, [1, 2, 3])

    def test_is_upper_tuple(self):
        self.assertRaises(TypeError, is_upper, (1, 2, 3))

    def test_is_upper_set(self):
        self.assertRaises(TypeError, is_upper, {1, 2, 3})

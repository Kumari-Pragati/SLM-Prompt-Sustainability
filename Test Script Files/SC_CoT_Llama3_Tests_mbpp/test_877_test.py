import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(sort_String('hello'), 'ehllo')
        self.assertEqual(sort_String('world'), 'dlrow')
        self.assertEqual(sort_String('abc'), 'abc')

    def test_edge_cases(self):
        self.assertEqual(sort_String(''), '')
        self.assertEqual(sort_String('a'), 'a')
        self.assertEqual(sort_String('abcde'), 'abcde')

    def test_corner_cases(self):
        self.assertEqual(sort_String('aaabbc'), 'abcab')
        self.assertEqual(sort_String('aabbcc'), 'abcabc')
        self.assertEqual(sort_String('123456'), '123456')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sort_String(None)
        with self.assertRaises(TypeError):
            sort_String(123)

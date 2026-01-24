import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_replace_char(self):
        self.assertEqual(replace_char('hello', 'l', 'p'), 'heppo')
        self.assertEqual(replace_char('world', 'o', 'x'), 'wirld')
        self.assertEqual(replace_char('test', 't', 'z'), 'zes')
        self.assertEqual(replace_char('python', 'n', 'm'), 'pym')
        self.assertEqual(replace_char('unittest', 'n', 'm'), 'unittest')
        self.assertEqual(replace_char('', 'a', 'b'), '')

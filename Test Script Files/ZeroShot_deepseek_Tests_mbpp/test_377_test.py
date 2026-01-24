import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_remove_Char(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')
        self.assertEqual(remove_Char('world', 'o'), 'wrld')
        self.assertEqual(remove_Char('python', 'n'), 'pytho')
        self.assertEqual(remove_Char('unittest', 't'), 'unitc')
        self.assertEqual(remove_Char('abcabc', 'b'), 'acac')
        self.assertEqual(remove_Char('aaaa', 'a'), '')
        self.assertEqual(remove_Char('hello', 'z'), 'hello')

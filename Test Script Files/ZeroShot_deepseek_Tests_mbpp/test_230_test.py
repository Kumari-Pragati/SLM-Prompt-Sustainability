import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_replace_blank(self):
        self.assertEqual(replace_blank('Hello World', '+'), 'Hello+World')
        self.assertEqual(replace_blank('Python is fun', '-'), 'Python-is-fun')
        self.assertEqual(replace_blank('This is a test', '*'), 'This*is*a*test')
        self.assertEqual(replace_blank('No blanks here', '#'), 'No#blanks#here')

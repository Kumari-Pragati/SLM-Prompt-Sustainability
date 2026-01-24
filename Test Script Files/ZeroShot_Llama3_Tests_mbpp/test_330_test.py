import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_find_char(self):
        self.assertEqual(find_char("Hello World"), ['World'])
        self.assertEqual(find_char("Python is awesome"), ['awesome'])
        self.assertEqual(find_char("I love to code"), ['code'])
        self.assertEqual(find_char("I am a developer"), ['developer'])
        self.assertEqual(find_char("I am a developer in Python"), ['developer', 'Python'])
        self.assertEqual(find_char("I am a developer in Python and I love to code"), ['developer', 'Python', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python"), ['developer', 'Python', 'Python', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python"), ['developer', 'Python', 'Python', 'Python', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code in Python and I love to code"), ['developer', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code'])
        self.assertEqual(find_char("I am a developer in Python and I love to code in Python and I love
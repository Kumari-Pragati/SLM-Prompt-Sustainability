import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_replace_spaces(self):
        self.assertEqual(replace_spaces('Hello World'), 'Hello%20World')
        self.assertEqual(replace_spaces('Python is awesome'), 'Python%20is%20awesome')
        self.assertEqual(replace_spaces('   spacious   '), '%20spacious%20')
        self.assertEqual(replace_spaces(''), '')
        self.assertEqual(replace_spaces('a'*1001), -1)
        self.assertEqual(replace_spaces('a'*1000), 'a'*1000)
        self.assertEqual(replace_spaces('a b c'), 'a%20b%20c')
        self.assertEqual(replace_spaces('a b c d e f g h i j k l m n o p q r s t u v w x y z'), 'a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o%20p%20q%20r%20s%20t%20u%20v%20w%20x%20y%20z')

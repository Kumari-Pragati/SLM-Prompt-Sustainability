import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(replace_spaces("Hello"), "Hello")
        self.assertEqual(replace_spaces("   "), "   ")
        self.assertEqual(replace_spaces(""), "")

    def test_edge(self):
        self.assertEqual(replace_spaces("a"), "a")
        self.assertEqual(replace_spaces("a b"), "a%20b")
        self.assertEqual(replace_spaces("a b c"), "a%20b%20c")
        self.assertEqual(replace_spaces("a b c d"), "a%20b%20c%20d")
        self.assertEqual(replace_spaces("a b c d e"), "a%20b%20c%20d%20e")
        self.assertEqual(replace_spaces("a b c d e f"), "a%20b%20c%20d%20e%20f")
        self.assertEqual(replace_spaces("a b c d e f g"), "a%20b%20c%20d%20e%20f%20g")
        self.assertEqual(replace_spaces("a b c d e f g h"), "a%20b%20c%20d%20e%20f%20g%20h")
        self.assertEqual(replace_spaces("a b c d e f g h i"), "a%20b%20c%20d%20e%20f%20g%20h%20i")
        self.assertEqual(replace_spaces("a b c d e f g h i j"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j")
        self.assertEqual(replace_spaces("a b c d e f g h i j k"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o%20p")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o%20p%20q")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o%20p%20q%20r")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s"), "a%20b%20c%20d%20e%20f%20g%20h%20i%20j%20k%20l%20m%20n%20o%20p%20q%20r%20s")
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t"), "a%20b%20c%20d%20e%20f%20g%20
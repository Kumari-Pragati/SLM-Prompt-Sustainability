import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_spaces("Hello World"), "0%20World")

    def test_edge_case1(self):
        self.assertEqual(replace_spaces("a"), "a")

    def test_edge_case2(self):
        self.assertEqual(replace_spaces("a b c"), "0%20b%20c")

    def test_edge_case3(self):
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t u v w x y z"), "0%20q%20r%20s%20t%20u%20v%20w%20x%20y%20z")

    def test_edge_case4(self):
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"), "0%20q%20r%20s%20t%20u%20v%20w%20x%20y%20z")

    def test_error_case1(self):
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z")*2, -1)

    def test_error_case2(self):
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"*1000), -1)

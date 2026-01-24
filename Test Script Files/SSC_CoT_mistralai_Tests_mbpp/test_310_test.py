import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(string_to_tuple("hello world"), ("hello", "world"))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(string_to_tuple(""), ())
        self.assertEqual(string_to_tuple("   "), ("",))
        self.assertEqual(string_to_tuple("a b c d e f g h i j k l m n o p q r s t u v w x y z"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))
        self.assertEqual(string_to_tuple("a\tb\nc\td\ne\tf\tg\th\ti\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tu\tv\tw\tx\ty\tz"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))
        self.assertEqual(string_to_tuple("a\t\tb\tc\t\td\te\tf\t\tg\th\ti\t\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tu\tv\tw\tx\ty\tz"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))

    def test_special_cases(self):
        self.assertEqual(string_to_tuple("a\tb\tc\td\te\tf\tg\th\ti\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tu\tv\tw\tx\ty\tz\n"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))
        self.assertEqual(string_to_tuple("a\tb\tc\td\te\tf\tg\th\ti\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tu\tv\tw\tx\ty\tz\n\n"), ())
        self.assertEqual(string_to_tuple("a\tb\tc\td\te\tf\tg\th\ti\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tu\tv\tw\tx\ty\tz\n\n\n"), ())

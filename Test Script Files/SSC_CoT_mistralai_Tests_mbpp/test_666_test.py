import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_char("hello", "l"), 3)
        self.assertEqual(count_char("Python", "h"), 1)
        self.assertEqual(count_char("12345", "5"), 1)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_char("", "a"), 0)
        self.assertEqual(count_char("abc", "z"), 0)
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("aaaa", "a"), 4)
        self.assertEqual(count_char("python", "y"), 0)

    def test_special_cases(self):
        self.assertEqual(count_char("Python", "P"), 1)
        self.assertEqual(count_char("Python", "o"), 1)
        self.assertEqual(count_char("Python", "T"), 1)
        self.assertEqual(count_char("Python", "Pp"), 2)
        self.assertEqual(count_char("Python", "Py"), 1)

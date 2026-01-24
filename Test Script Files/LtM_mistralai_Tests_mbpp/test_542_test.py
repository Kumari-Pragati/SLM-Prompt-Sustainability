import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(fill_spaces("hello, world."), "hello:world:")
        self.assertEqual(fill_spaces("Python is awesome!"), "Python:is:awesome:!")

    def test_edge_input(self):
        self.assertEqual(fill_spaces(""), "")
        self.assertEqual(fill_spaces(" , "), ":")
        self.assertEqual(fill_spaces(".,,"), ":::")
        self.assertEqual(fill_spaces("Python,Python,Python"), "Python:Python:Python")

    def test_complex_input(self):
        self.assertEqual(fill_spaces("hello, world. It's a beautiful day, isn't it?"),
                         "hello:world.It's:a:beautiful:day,:isn't:it:?")
        self.assertEqual(fill_spaces("Python isn't it? Python!"), "Python:isn't:it?:Python!")

import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(replace_blank("Hello World", '*'), "Hello*World")
        self.assertEqual(replace_blank("Python is fun", '_'), "Python_is_fun")
        self.assertEqual(replace_blank("Replace blank",''), "Replace blank")

    def test_edge_cases(self):
        self.assertEqual(replace_blank("", '*'), "")
        self.assertEqual(replace_blank("Hello", '*'), "Hello")
        self.assertEqual(replace_blank("   ", '*'), "*"*4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_blank(None, '*')
        with self.assertRaises(TypeError):
            replace_blank("Hello", None)

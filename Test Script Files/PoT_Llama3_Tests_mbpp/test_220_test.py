import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 2), "Hello:world!")

    def test_edge_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 0), "Hello, world!")

    def test_edge_case2(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 10), "Hello:world!")

    def test_edge_case3(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", -1), "Hello, world!")

    def test_corner_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 1), "Hello:world!")

    def test_corner_case2(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 3), "Hello:world!")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar(123, 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, world!", 'a')

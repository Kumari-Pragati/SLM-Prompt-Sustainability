import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge2(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge3(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge4(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge5(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge6(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge7(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge8(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge9(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

    def test_edge10(self):
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")
        self.assertEqual(replace("hello world hello world", 'o'), "hello world hello world")

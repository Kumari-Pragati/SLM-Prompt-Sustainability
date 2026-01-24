import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HELLOWORLD")

    def test_edge_cases(self):
        self.assertEqual(remove_lowercase(""), "")
        self.assertEqual(remove_lowercase("A"), "A")
        self.assertEqual(remove_lowercase("Aa"), "A")
        self.assertEqual(remove_lowercase("Zz"), "ZZ")
        self.assertEqual(remove_lowercase("HelloWorld123"), "HELLOWORLD123")

    def test_boundary_cases(self):
        self.assertEqual(remove_lowercase("A_"), "A_")
        self.assertEqual(remove_lowercase("_A"), "_A")
        self.assertEqual(remove_lowercase("_A_"), "_A_")
        self.assertEqual(remove_lowercase("A_B"), "A_B")
        self.assertEqual(remove_lowercase("B_A"), "B_A")

    def test_special_cases(self):
        self.assertEqual(remove_lowercase("HeLlO wOrLd"), "HELLO WORLD")
        self.assertEqual(remove_lowercase("HeLlO wOrLd123"), "HELLO WORLD123")
        self.assertEqual(remove_lowercase("HeLlO wOrLd!@#$%^&*()"), "HELLO WORLD!@#$%^&*()")

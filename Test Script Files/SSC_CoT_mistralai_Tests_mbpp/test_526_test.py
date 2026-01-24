import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")
        self.assertEqual(capitalize_first_last_letters("HELLO WORLD"), "Hello World")
        self.assertEqual(capitalize_first_last_letters("Hello World!"), "Hello World!")

    def test_edge_cases(self):
        self.assertEqual(capitalize_first_last_letters(""), "")
        self.assertEqual(capitalize_first_last_letters(" "), " ")
        self.assertEqual(capitalize_first_last_letters("A"), "A")
        self.assertEqual(capitalize_first_last_letters("a"), "A")
        self.assertEqual(capitalize_first_last_letters("A B"), "A B")
        self.assertEqual(capitalize_first_last_letters("A B C"), "A B C")
        self.assertEqual(capitalize_first_last_letters("A B C D"), "A B C D")
        self.assertEqual(capitalize_first_last_letters("A B C D E"), "A B C D E")

    def test_special_cases(self):
        self.assertEqual(capitalize_first_last_letters("A-B"), "A-B")
        self.assertEqual(capitalize_first_last_letters("A-B C"), "A-B C")
        self.assertEqual(capitalize_first_last_letters("A-B C-D"), "A-B C-D")
        self.assertEqual(capitalize_first_last_letters("A_B"), "A_B")
        self.assertEqual(capitalize_first_last_letters("A_B C"), "A_B C")
        self.assertEqual(capitalize_first_last_letters("A_B C_D"), "A_B C_D")

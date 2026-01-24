import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_parenthesis(""), "")

    def test_single_item(self):
        self.assertEqual(remove_parenthesis("A"), "A")
        self.assertEqual(remove_parenthesis("(A)"), "A")
        self.assertEqual(remove_parenthesis("(A)B"), "A B")
        self.assertEqual(remove_parenthesis("A(B)"), "A B")

    def test_multiple_items(self):
        self.assertEqual(remove_parenthesis(["A", "(B)", "C(D)"]), ["A", "B", "C D"])

    def test_nested_parentheses(self):
        self.assertEqual(remove_parenthesis("((A))"), "A")
        self.assertEqual(remove_parenthesis("A((B))C"), "A B C")
        self.assertEqual(remove_parenthesis("A((B)C)D"), "A B C D")

    def test_mixed_string_and_parentheses(self):
        self.assertEqual(remove_parenthesis("A(B)C(D)"), "A B C D")
        self.assertEqual(remove_parenthesis("A(B)C(D)E"), "A B C D E")
        self.assertEqual(remove_parenthesis("A(B)C(D)E(F)"), "A B C D E F")

    def test_empty_list(self):
        self.assertEqual(remove_parenthesis([]), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_parenthesis, 123)
        self.assertRaises(TypeError, remove_parenthesis, (1, 2, 3))

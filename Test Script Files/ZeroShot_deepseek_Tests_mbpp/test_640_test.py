import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis(["Hello (World)"]), ["Hello "])
        self.assertEqual(remove_parenthesis(["Hello (World) and (Earth)"]) , ["Hello "])
        self.assertEqual(remove_parenthesis(["No parenthesis here"]) , ["No parenthesis here"])
        self.assertEqual(remove_parenthesis(["(Just open) and (Just close)"]) , [" "])
        self.assertEqual(remove_parenthesis(["(Open and Close)"]), [" "])

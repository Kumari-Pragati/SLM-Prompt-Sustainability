import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_add_string(self):
        self.assertEqual(add_string(['apple', 'banana', 'cherry'], 'I like {}'), ['I like apple', 'I like banana', 'I like cherry'])
        self.assertEqual(add_string(['dog', 'cat', 'mouse'], 'I have a {}'), ['I have a dog', 'I have a cat', 'I have a mouse'])
        self.assertEqual(add_string(['red', 'green', 'blue'], 'My favorite color is {}'), ['My favorite color is red', 'My favorite color is green', 'My favorite color is blue'])

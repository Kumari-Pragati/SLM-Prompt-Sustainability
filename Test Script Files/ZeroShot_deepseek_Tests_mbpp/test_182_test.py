import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_find_character(self):
        self.assertEqual(find_character("HelloWorld123!"), 
                         (['H', 'W', 'O', 'R', 'D'], ['e', 'l', 'l', 'o', 'r', 'l', 'd'], ['1', '2', '3'], [',' ,'.', '!']))
        self.assertEqual(find_character("aBC123$%^&*()"), 
                         (['B', 'C'], ['a', 'b', 'c', '1', '2', '3'], [], [',' ,'.', '!']))
        self.assertEqual(find_character("1234567890"), 
                         ([],[],[['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']], []))
        self.assertEqual(find_character("!@#$%^&*()"), 
                         ([],[],[],[',' ,'.', '!']))
        self.assertEqual(find_character(""), 
                         ([],[],[],[]))

import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_character("HelloWorld123"), 
                         (['H', 'W'], ['e', 'o', 'l', 'l', 'o', 'r', 'd'], ['1', '2', '3'], [',' ,'.', '!', '?']))

    def test_empty_string(self):
        self.assertEqual(find_character(""), ([], [], [], []))

    def test_all_characters(self):
        self.assertEqual(find_character("ABCabc123, .!?!"), 
                         (['A', 'B', 'C'], ['a', 'b', 'c'], ['1', '2', '3'], [',' ,'.', '!', '?']))

    def test_no_uppercase(self):
        self.assertEqual(find_character("helloWorld123, .!?!"), 
                         ([], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'], ['1', '2', '3'], [',' ,'.', '!', '?']))

    def test_no_lowercase(self):
        self.assertEqual(find_character("HELLOWorld123, .!?!"), 
                         (['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D'], [], ['1', '2', '3'], [',' ,'.', '!', '?']))

    def test_no_numbers(self):
        self.assertEqual(find_character("HelloWorld, .!?!"), 
                         (['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D'], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'], [], [',' ,'.', '!', '?']))

    def test_no_special_characters(self):
        self.assertEqual(find_character("HelloWorld123"), 
                         (['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D'], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'], ['1', '2', '3'], []))

import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_character("Hello World"), (["H", "W"], ["e", "o"], [""], ["o", "!"]))
        self.assertEqual(find_character("123456"), ([""], [""], ["1", "2", "3", "4", "5", "6"], ""))
        self.assertEqual(find_character(".,!?"), ([""], [""], [""], [".,!?"]))

    def test_edge_cases(self):
        self.assertEqual(find_character(""), ([""], [""], [""], ""))
        self.assertEqual(find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [], [], ""))
        self.assertEqual(find_character("abcdefghijklmnopqrstuvwxyz"), ([""], list("abcdefghijklmnopqrstuvwxyz"), [], ""))
        self.assertEqual(find_character("0123456789"), ([""], [""], list("0123456789"), ""))
        self.assertEqual(find_character(".,!? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789"), ([""], [""], list("0123456789"), [".,!?"]))

    def test_complex_inputs(self):
        self.assertEqual(find_character("Hello World, ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789"), (["H", "W"], ["e", "o"], ["1", "2", "3", "4", "5", "6"], ["o", "!"]))
        self.assertEqual(find_character(".,!? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789"), ([""], [""], list("0123456789"), [".,!?"]))

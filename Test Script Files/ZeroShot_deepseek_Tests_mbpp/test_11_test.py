import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_remove_Occ(self):
        self.assertEqual(remove_Occ('hello', 'l'), 'helo')
        self.assertEqual(remove_Occ('world', 'o'), 'wrld')
        self.assertEqual(remove_Occ('python', 'n'), 'pytho')
        self.assertEqual(remove_Occ('unittest', 't'), 'unites')
        self.assertEqual(remove_Occ('aaa', 'a'), '')
        self.assertEqual(remove_Occ('abc', 'd'), 'abc')
        self.assertEqual(remove_Occ('aaa', 'b'), 'aaa')
        self.assertEqual(remove_Occ('aaa', 'c'), 'aaa')

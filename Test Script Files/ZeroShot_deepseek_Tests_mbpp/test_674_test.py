import unittest
from mbpp_674_code import OrderedDict
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_remove_duplicate(self):
        self.assertEqual(remove_duplicate('hello world'), 'hello world')
        self.assertEqual(remove_duplicate('hello hello world'), 'hello world')
        self.assertEqual(remove_duplicate('hello world world'), 'hello world')
        self.assertEqual(remove_duplicate('hello hello world world'), 'hello world')
        self.assertEqual(remove_duplicate(''), '')
        self.assertEqual(remove_duplicate('a b c d'), 'a b c d')
        self.assertEqual(remove_duplicate('a a b b c c d d'), 'a b c d')

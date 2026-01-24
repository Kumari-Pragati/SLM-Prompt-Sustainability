import unittest
from mbpp_326_code import defaultdict
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_most_occurrences(self):
        test_list = ['hello world', 'hello python', 'world python']
        self.assertEqual(most_occurrences(test_list), 'python')

        test_list = ['apple orange', 'orange banana', 'banana apple']
        self.assertEqual(most_occurrences(test_list), 'apple')

        test_list = ['one two', 'two three', 'three one']
        self.assertEqual(most_occurrences(test_list), 'one')

        test_list = ['a b', 'b c', 'c a']
        self.assertEqual(most_occurrences(test_list), 'a')

        test_list = ['1 2', '2 3', '3 1']
        self.assertEqual(most_occurrences(test_list), '1')

        test_list = ['']
        self.assertEqual(most_occurrences(test_list), '')

        test_list = []
        self.assertEqual(most_occurrences(test_list), '')

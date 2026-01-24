import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_count_variable(self):
        self.assertEqual(count_variable('a', 'b', 'c', 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(count_variable('a', 'a', 'c', 'd'), ['a', 'a', 'c', 'd'])
        self.assertEqual(count_variable('a', 'b', 'c', 'c'), ['a', 'b', 'c', 'c'])
        self.assertEqual(count_variable('a', 'a', 'c', 'c'), ['a', 'a', 'c', 'c'])
        self.assertEqual(count_variable('a', 'b', 'c', 'd', 'e'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(count_variable('a', 'a', 'c', 'c', 'e'), ['a', 'a', 'c', 'c', 'e'])

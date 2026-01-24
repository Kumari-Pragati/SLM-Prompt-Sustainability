import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_second_frequent(self):
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'orange']), 'banana')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana']), 'apple')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana', 'banana']), 'apple')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana', 'banana', 'banana']), 'apple')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana', 'banana', 'banana', 'banana']), 'banana')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana']), 'apple')
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana']), 'banana')

    def test_empty_list(self):
        self.assertEqual(second_frequent([]), None)

    def test_single_element_list(self):
        self.assertEqual(second_frequent(['apple']), 'apple')

    def test_all_same_element_list(self):
        self.assertEqual(second_frequent(['apple', 'apple', 'apple', 'apple', 'apple']), 'apple')

import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'orange', 'banana']), 'banana')

    def test_edge_case(self):
        self.assertEqual(second_frequent(['apple', 'apple', 'apple', 'apple']), '1')

    def test_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_single_element_list(self):
        self.assertEqual(second_frequent(['apple']), 'apple')

    def test_multiple_frequent_elements(self):
        self.assertEqual(second_frequent(['apple', 'banana', 'apple', 'banana', 'orange']), 'banana')

    def test_no_frequent_elements(self):
        self.assertIsNone(second_frequent(['apple', 'banana', 'orange', 'grape','mango']))

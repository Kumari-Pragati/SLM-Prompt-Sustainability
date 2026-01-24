import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_tuplex([], 1), 0)

    def test_single_element(self):
        self.assertEqual(count_tuplex([1], 1), 1)
        self.assertEqual(count_tuplex([2], 1), 0)

    def test_multiple_elements(self):
        self.assertEqual(count_tuplex([1, 2, 1, 3, 1], 1), 3)
        self.assertEqual(count_tuplex([1, 2, 1, 3, 1], 2), 0)
        self.assertEqual(count_tuplex([1, 2, 1, 3, 1], 3), 1)

    def test_duplicates(self):
        self.assertEqual(count_tuplex([1, 1, 1, 2, 2, 3, 3, 3], 1), 3)
        self.assertEqual(count_tuplex([1, 1, 1, 2, 2, 3, 3, 3], 2), 2)
        self.assertEqual(count_tuplex([1, 1, 1, 2, 2, 3, 3, 3], 3), 3)

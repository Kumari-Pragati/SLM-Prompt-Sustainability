import unittest
from mbpp_946_code import Counter
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_most_common_elem(self):
        self.assertEqual(most_common_elem('aabbbcc', 1), [('b', 3)])
        self.assertEqual(most_common_elem('aabbbcc', 2), [('b', 3), ('a', 2)])
        self.assertEqual(most_common_elem('aabbbcc', 3), [('b', 3), ('a', 2), ('c', 2)])
        self.assertEqual(most_common_elem('aabbbcc', 4), [('b', 3), ('a', 2), ('c', 2)])
        self.assertEqual(most_common_elem('aabbbcc', 5), [('b', 3), ('a', 2), ('c', 2)])
        self.assertEqual(most_common_elem('aabbbcc', 6), [('b', 3), ('a', 2), ('c', 2)])
        self.assertEqual(most_common_elem('aabbbcc', 7), [('b', 3), ('a', 2), ('c', 2)])

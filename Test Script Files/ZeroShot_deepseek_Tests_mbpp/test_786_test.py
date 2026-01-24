import unittest
from mbpp_786_code import bisect_right

def right_insertion(a, x):
    i = bisect_right(a, x)
    return i

class TestRightInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 5), 0)

    def test_single_element(self):
        self.assertEqual(right_insertion([3], 5), 1)
        self.assertEqual(right_insertion([5], 5), 1)

    def test_multiple_elements(self):
        self.assertEqual(right_insertion([1, 3, 5], 0), 0)
        self.assertEqual(right_insertion([1, 3, 5], 2), 1)
        self.assertEqual(right_insertion([1, 3, 5], 3), 1)
        self.assertEqual(right_insertion([1, 3, 5], 5), 2)
        self.assertEqual(right_insertion([1, 3, 5], 7), 3)

    def test_duplicate_elements(self):
        self.assertEqual(right_insertion([1, 1, 3, 5], 1), 2)
        self.assertEqual(right_insertion([1, 3, 5, 5], 5), 3)

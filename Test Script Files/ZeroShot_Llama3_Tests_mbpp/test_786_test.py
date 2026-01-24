import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_right_insertion(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 6), 5)

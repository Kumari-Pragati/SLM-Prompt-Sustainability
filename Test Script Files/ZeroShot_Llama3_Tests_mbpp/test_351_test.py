import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_first_element(self):
        self.assertEqual(first_Element([1, 2, 3, 2, 3, 1, 3], 7, 2), 3)
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1], 5, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6], 6, 2), 2)
        self.assertEqual(first_Element([1, 1, 2, 2, 3, 3], 6, 2), 2)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7], 7, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1], 7, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7, 8], 8, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1], 8, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1], 9, 1), 1)
        self.assertEqual(first_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 1), 1)
        self.assertEqual(first_Element([], 0, 1), -1)
        self.assertEqual(first_Element([1], 1, 1), 1)
        self.assertEqual(first_Element([1, 2], 2, 1), 1)
        self.assertEqual(first_Element([1, 1], 2, 1), 1)
        self.assertEqual(first_Element([1, 1, 1], 3, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1], 4, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1], 5, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1], 6, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1], 7, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1], 8, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1], 9, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 12, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13, 1), 1)
        self.assertEqual(first_Element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1
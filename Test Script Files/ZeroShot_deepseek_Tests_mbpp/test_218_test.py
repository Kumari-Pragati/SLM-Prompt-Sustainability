import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_swap(self):
        self.assertEqual(min_Operations(5, 3), 2)
        self.assertEqual(min_Operations(10, 2), 1)
        self.assertEqual(min_Operations(15, 15), 0)

    def test_B_greater_than_A(self):
        self.assertEqual(min_Operations(3, 7), 2)
        self.assertEqual(min_Operations(2, 10), 1)
        self.assertEqual(min_Operations(5, 15), 0)

    def test_B_equal_to_A(self):
        self.assertEqual(min_Operations(2, 2), 0)
        self.assertEqual(min_Operations(10, 10), 0)
        self.assertEqual(min_Operations(15, 15), 0)

    def test_B_is_multiple_of_A(self):
        self.assertEqual(min_Operations(2, 4), 1)
        self.assertEqual(min_Operations(5, 25), 1)
        self.assertEqual(min_Operations(10, 100), 9)

import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_typical(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 1
        right_element = 10
        self.assertEqual(smallest_missing(A, left_element, right_element), 4)

    def test_edge_left(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 10
        right_element = 10
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_edge_right(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 1
        right_element = 1
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element + 1)

    def test_edge_equal(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 1
        right_element = 1
        self.assertEqual(smallest_missing(A, left_element, right_element), 2)

    def test_special(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 2
        right_element = 5
        self.assertEqual(smallest_missing(A, left_element, right_element), 4)

    def test_invalid_left(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 11
        right_element = 10
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_invalid_right(self):
        A = [1, 2, 3, 5, 6, 7, 9, 10]
        left_element = 1
        right_element = 0
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element + 1)

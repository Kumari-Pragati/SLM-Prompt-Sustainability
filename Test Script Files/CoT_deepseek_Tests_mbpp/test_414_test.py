import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(overlapping([1, 2, 3], [2, 3, 4]), 1)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(overlapping([1, 2, 2, 3], [2, 3, 4]), 1)

    def test_typical_case_with_reversed_order(self):
        self.assertEqual(overlapping([3, 2, 1], [2, 3, 4]), 1)

    def test_no_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], [2]), 0)

    def test_large_lists(self):
        self.assertEqual(overlapping(list(range(1, 10001)), list(range(10001, 20001))), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            overlapping(123, [1, 2, 3])
        with self.assertRaises(TypeError):
            overlapping([1, 2, 3], '123')

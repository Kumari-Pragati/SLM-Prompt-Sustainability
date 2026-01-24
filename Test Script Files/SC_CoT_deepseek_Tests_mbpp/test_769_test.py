import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [[1], [4]])

    def test_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(Diff([1, 2, 3], []), [[1, 2, 3]])
        self.assertEqual(Diff([], [1, 2, 3]), [[1, 2, 3]])

    def test_duplicate_elements(self):
        self.assertEqual(Diff([1, 2, 2, 3], [2, 2, 3, 4]), [[1], [4]])

    def test_same_elements(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Diff(123, [1, 2, 3])
        with self.assertRaises(TypeError):
            Diff([1, 2, 3], 123)

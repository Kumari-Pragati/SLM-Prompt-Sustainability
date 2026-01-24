import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_start(self):
        self.assertEqual(remove_duplicate([2, 1, 2]), [1, 2])

    def test_duplicate_end(self):
        self.assertEqual(remove_duplicate([1, 2, 2]), [1, 2])

    def test_duplicate_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 1]), [1, 2])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicate([-1, -2, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplicate([1, -2, 2, -3, 4]), [1, -2, 2, 4])

    def test_duplicate_floats(self):
        self.assertEqual(remove_duplicate([1.1, 2.2, 2.2, 3.3]), [1.1, 2.2, 3.3])

    def test_duplicate_strings(self):
        self.assertEqual(remove_duplicate(['a', 'b', 'b', 'c']), ['a', 'b', 'c'])

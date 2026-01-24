import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(remove_elements([], []), [])
        self.assertEqual(remove_elements([], [1, 2, 3]), [])
        self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertEqual(remove_elements([1], [1]), [])
        self.assertEqual(remove_elements([1], []), [1])
        self.assertEqual(remove_elements([1, 2], [1]), [2])
        self.assertEqual(remove_elements([1, 2], [2]), [1])

    def test_duplicates(self):
        self.assertEqual(remove_elements([1, 1, 2, 2, 3], [1, 2]), [3])
        self.assertEqual(remove_elements([1, 1, 2, 2, 3], [1, 1, 2, 2]), [])

    def test_order_matters(self):
        self.assertEqual(remove_elements([1, 2, 3], [2, 3]), [1])
        self.assertEqual(remove_elements([1, 2, 3], [3, 2]), [1])

    def test_large_lists(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5]), [6, 7, 8, 9, 10])

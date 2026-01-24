import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([], [1, 2, 3]), [])
        self.assertListEqual(remove_elements([1, 2, 3], []), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], [2, 3]), [1])
        self.assertListEqual(remove_elements([2, 3], [1]), [2, 3])

    def test_contained_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3, 4], [2, 3]), [1, 4])
        self.assertListEqual(remove_elements([1, 2, 3, 4], [4, 5]), [1, 2, 3])
        self.assertListEqual(remove_elements([1, 2, 3, 4], [1, 2]), [3, 4])

    def test_multiple_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [2, 3, 6]), [1, 4, 5])
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [1, 4, 6]), [2, 3, 5])
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 5]), [3, 4])

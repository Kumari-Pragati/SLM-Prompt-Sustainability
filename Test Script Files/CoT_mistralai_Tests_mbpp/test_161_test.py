import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([], [1]), [])
        self.assertListEqual(remove_elements([], [1, 2, 3]), [])

    def test_single_element_lists(self):
        self.assertListEqual(remove_elements([1], []), [1])
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], [2, 3]), [1])

    def test_lists_with_common_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3, 1, 2], [1, 2]), [3])
        self.assertListEqual(remove_elements([1, 2, 3, 1, 2], [2, 3]), [1])
        self.assertListEqual(remove_elements([1, 2, 3, 1, 2], [3, 1]), [2])

    def test_lists_with_no_common_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3], [4, 5, 6]), [1, 2, 3])
        self.assertListEqual(remove_elements([4, 5, 6], [1, 2, 3]), [4, 5, 6])

    def test_lists_with_duplicates(self):
        self.assertListEqual(remove_elements([1, 1, 2, 3, 1], [1, 2]), [2, 3])
        self.assertListEqual(remove_elements([1, 1, 2, 3, 1], [2, 3]), [1])
        self.assertListEqual(remove_elements([1, 1, 2, 3, 1], [3, 1]), [2])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_elements, 1, [1])
        self.assertRaises(TypeError, remove_elements, [1], 1)

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

    def test_lists_with_matching_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3], [1, 2]), [3])
        self.assertListEqual(remove_elements([1, 2, 3], [2, 1]), [3])
        self.assertListEqual(remove_elements([1, 2, 3], [3, 2, 1]), [1])

    def test_lists_with_non_matching_elements(self):
        self.assertListEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])
        self.assertListEqual(remove_elements([4, 5], [1, 2, 3]), [])

    def test_lists_with_duplicates(self):
        self.assertListEqual(remove_elements([1, 1, 2, 3], [1, 2]), [3, 2])
        self.assertListEqual(remove_elements([1, 1, 2, 3], [2, 1]), [3])

    def test_lists_with_long_elements(self):
        self.assertListEqual(remove_elements(["a", "b", "c"], ["b", "a"]), ["c"])
        self.assertListEqual(remove_elements(["b", "a"], ["a", "b"]), [])

    def test_lists_with_mixed_types(self):
        self.assertListEqual(remove_elements([1, "a", 2], [2, "a"]), [1])
        self.assertListEqual(remove_elements([2, "a"], [1, "a"]), [2])

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            remove_elements(None, [1])
        with self.assertRaises(TypeError):
            remove_elements([1], None)

import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(remove_elements([], []), [])

    def test_single_element_list1(self):
        self.assertEqual(remove_elements([1], []), [1])

    def test_single_element_list2(self):
        self.assertEqual(remove_elements([], [1]), [])

    def test_multiple_elements_list1(self):
        self.assertEqual(remove_elements([1, 2, 3], [2]), [1, 3])

    def test_multiple_elements_list2(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 3]), [2])

    def test_duplicates_in_list1(self):
        self.assertEqual(remove_elements([1, 1, 2, 2, 3], [1, 2]), [3])

    def test_duplicates_in_list2(self):
        self.assertEqual(remove_elements([1, 1, 2, 2, 3], [1, 1, 2]), [3])

    def test_empty_list1(self):
        self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3])

    def test_empty_list2(self):
        self.assertEqual(remove_elements([], [1, 2, 3]), [])

    def test_list1_longer_than_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2]), [3, 4, 5])

    def test_list2_longer_than_list1(self):
        self.assertEqual(remove_elements([1, 2], [1, 2, 3, 4, 5]), [])

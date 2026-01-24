import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [2, 4]), [1, 3])

    def test_empty_lists(self):
        self.assertEqual(remove_elements([], []), [])

    def test_all_elements_in_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [1, 2, 3, 4]), [])

    def test_duplicates_in_list2(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4], [2]), [1, 2, 3, 4])

    def test_duplicates_in_list1(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4], [2, 2]), [1, 3, 4])

    def test_single_element_lists(self):
        self.assertEqual(remove_elements([1], [1]), [])
        self.assertEqual(remove_elements([1], []), [1])

    def test_large_lists(self):
        self.assertEqual(remove_elements(list(range(1, 1001)), list(range(500, 1501))), list(range(1, 500)) + list(range(1501, 1001)))

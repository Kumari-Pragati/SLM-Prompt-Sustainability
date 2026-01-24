import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_simple_case(self):
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])

    def test_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([1, 2, 3], []), [1, 2, 3])
        self.assertListEqual(remove_elements([], [1, 2, 3]), [])

    def test_single_element(self):
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], [2]), [1])

    def test_edge_case_min(self):
        self.assertListEqual(remove_elements([-100], [-100, -99]), [])

    def test_edge_case_max(self):
        self.assertListEqual(remove_elements([9999], [10000, 9999]), [])

    def test_duplicates(self):
        self.assertListEqual(remove_elements([1, 1, 2, 3], [1, 2]), [3])

    def test_negative_numbers(self):
        self.assertListEqual(remove_elements([-1, 0, 1], [-1, 0]), [1])

    def test_mixed_numbers(self):
        self.assertListEqual(remove_elements([1, 'a', 2, 'b', 3], [2, 'b']), [1, 'a', 3])

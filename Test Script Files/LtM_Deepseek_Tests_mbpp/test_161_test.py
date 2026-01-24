import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(remove_elements([1, 2, 3], [2, 3]), [1])

    def test_empty_lists(self):
        self.assertEqual(remove_elements([], []), [])
        self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(remove_elements([], [1, 2, 3]), [])

    def test_all_elements_in_second_list(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

    def test_duplicate_elements(self):
        self.assertEqual(remove_elements([1, 2, 2, 3], [2]), [1, 2, 3])

    def test_complex_case(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 3, 5]), [1, 4])

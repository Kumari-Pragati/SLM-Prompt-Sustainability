import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_remove_elements(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [3, 4]), [1, 2, 5])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5])
        self.assertEqual(remove_elements([], [3, 4]), [])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]), [])

    def test_remove_elements_empty_list(self):
        self.assertEqual(remove_elements([], []), [])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5])
        self.assertEqual(remove_elements([], [1, 2, 3, 4, 5]), [])

    def test_remove_elements_single_element(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1]), [2, 3, 4, 5])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [5]), [1, 2, 3, 4])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2]), [1, 3, 4, 5])

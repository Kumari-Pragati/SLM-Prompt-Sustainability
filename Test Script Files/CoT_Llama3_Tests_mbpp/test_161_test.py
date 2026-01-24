import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_remove_elements(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 3]), [1, 4, 5])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5])
        self.assertEqual(remove_elements([], [2, 3]), [])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [6, 7, 8]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]), [])

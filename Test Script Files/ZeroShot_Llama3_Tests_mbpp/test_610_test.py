import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_remove_kth_element(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 2), [1, 2, 3, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [2, 3, 4, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

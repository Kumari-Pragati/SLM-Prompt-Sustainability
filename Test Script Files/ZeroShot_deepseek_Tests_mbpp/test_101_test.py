import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_kth_element(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 3), 10)
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 1), 3)
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 6), 20)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 3), 3)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 5), 1)
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 5, 1), 5)

import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(remove_even([1, 2, 3, 4]), [1, 3])
        self.assertEqual(remove_even([5, 6, 7, 8]), [5, 7])
        self.assertEqual(remove_even([10, 20, 30, 40]), [])
        self.assertEqual(remove_even([]), [])
        self.assertEqual(remove_even([1, 3, 5, 7]), [1, 3, 5, 7])

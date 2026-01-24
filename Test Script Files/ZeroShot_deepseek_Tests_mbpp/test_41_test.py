import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_filter_evennumbers(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_evennumbers([10, 20, 31, 42, 55, 66]), [10, 20, 42, 66])
        self.assertEqual(filter_evennumbers([1, 3, 5, 7, 9]), [])
        self.assertEqual(filter_evennumbers([]), [])
        self.assertEqual(filter_evennumbers([-2, -1, 0, 1, 2]), [0, 2])

import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_find_triplet_array(self):
        self.assertEqual(find_triplet_array([1, 4, 45, 6, 10, 8], 6, 22), (1, 4, 17))
        self.assertEqual(find_triplet_array([10, 20, 30, 40, 100], 5, 100), (10, 20, 70))
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 6), (1, 2, 3))
        self.assertEqual(find_triplet_array([1, 2, 3, 4, 5], 5, 10), False)
        self.assertEqual(find_triplet_array([], 0, 10), False)

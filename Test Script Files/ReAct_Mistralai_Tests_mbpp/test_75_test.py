import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_tuples([], 3), "[]")

    def test_single_element(self):
        self.assertEqual(find_tuples([1], 1), "[]")
        self.assertEqual(find_tuples([3], 3), "['3']")
        self.assertEqual(find_tuples([5], 2), "[]")

    def test_multiple_elements(self):
        self.assertEqual(find_tuples([0, 0, 0], 3), "['0', '0', '0']")
        self.assertEqual(find_tuples([1, 2, 3, 4], 2), "[]")
        self.assertEqual(find_tuples([4, 8, 12], 4), "['4', '8', '12']")
        self.assertEqual(find_tuples([1, 3, 5], 2), "[]")

    def test_negative_numbers(self):
        self.assertEqual(find_tuples([-3, -6, -9], 3), "['-3', '-6', '-9']")

    def test_floats(self):
        self.assertEqual(find_tuples([0.0, 3.0, 6.0], 3.0), "['0.0', '3.0', '6.0']")

    def test_large_numbers(self):
        self.assertEqual(find_tuples([1000000, 2000000, 3000000], 1000000), "['1000000', '2000000', '3000000']")

    def test_k_not_in_list(self):
        with self.assertRaises(ValueError):
            find_tuples([1, 2, 3], 4)

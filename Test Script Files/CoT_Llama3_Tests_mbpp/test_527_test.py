import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_get_pairs_count_typical(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 7
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_get_pairs_count_edge(self):
        arr = [1, 2, 3]
        n = len(arr)
        sum = 3
        self.assertEqual(get_pairs_count(arr, n, sum), 1)

    def test_get_pairs_count_edge2(self):
        arr = [1, 2, 3]
        n = len(arr)
        sum = 4
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_get_pairs_count_invalid_input(self):
        arr = [1, 2, 3]
        n = len(arr)
        sum = 'invalid'
        with self.assertRaises(TypeError):
            get_pairs_count(arr, n, sum)

    def test_get_pairs_count_empty_array(self):
        arr = []
        n = len(arr)
        sum = 5
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_get_pairs_count_single_element_array(self):
        arr = [1]
        n = len(arr)
        sum = 2
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

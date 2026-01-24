import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 6)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_boundary_case(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_special_case(self):
        arr = [1, 2, 2, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Pairs("1, 2, 3, 4, 5", 5)

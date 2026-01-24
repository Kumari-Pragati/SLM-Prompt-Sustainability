import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(search(arr, n), 0)

    def test_edge_case(self):
        arr = []
        n = 0
        self.assertEqual(search(arr, n), 0)

    def test_boundary_case(self):
        arr = [1]
        n = 1
        self.assertEqual(search(arr, n), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            search("not a list", 5)

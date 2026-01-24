import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_k([[1, 3], [2, 4], [3, 5]], 2), [[1, 3], [2, 4]])

    def test_edge_case(self):
        self.assertEqual(min_k([[1, 3], [2, 4], [3, 5]], 1), [[1, 3]])

    def test_edge_case2(self):
        self.assertEqual(min_k([[1, 3], [2, 4], [3, 5]], 3), [[1, 3], [2, 4], [3, 5]])

    def test_edge_case3(self):
        self.assertEqual(min_k([[1, 3], [2, 4], [3, 5]], 0), [])

    def test_edge_case4(self):
        self.assertEqual(min_k([[1, 3], [2, 4], [3, 5]], 5), [[1, 3], [2, 4], [3, 5]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_k("test", 2)

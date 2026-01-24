import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sort([(1, 2), (2, 1), (3, 2), (4, 1)]), [(4, 1), (3, 2), (2, 1), (1, 2)])

    def test_edge_case(self):
        self.assertEqual(Sort([]), [])

    def test_corner_case(self):
        self.assertEqual(Sort([(1, 2), (2, 1), (3, 2), (4, 1)]), [(4, 1), (3, 2), (2, 1), (1, 2)])
        self.assertEqual(Sort([(1, 1), (2, 2), (3, 3), (4, 4)]), [(4, 4), (3, 3), (2, 2), (1, 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Sort(123)
        with self.assertRaises(TypeError):
            Sort("string")
        with self.assertRaises(TypeError):
            Sort([1, 2, 3])

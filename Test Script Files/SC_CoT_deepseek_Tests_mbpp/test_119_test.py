import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case(self):
        self.assertEqual(search([], 0), 0)
        self.assertEqual(search([1], 1), 1)

    def test_corner_case(self):
        self.assertEqual(search([1, 1, 2, 2, 3], 5), 3)
        self.assertEqual(search([1, 2, 3, 4, 4], 5), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            search("1, 2, 3, 4, 5", 5)
        with self.assertRaises(TypeError):
            search([1, 2, 3, 4, 5], "5")
        with self.assertRaises(TypeError):
            search([1, 2, 3, "4", 5], 5)

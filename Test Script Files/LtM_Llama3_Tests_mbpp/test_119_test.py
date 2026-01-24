import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6], 6), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7], 7), 0)

    def test_edge_cases(self):
        self.assertEqual(search([], 0), 0)
        self.assertEqual(search([1], 1), 1)
        self.assertEqual(search([1, 2], 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            search("abc", 5)
        with self.assertRaises(TypeError):
            search([1, 2, 3], "abc")

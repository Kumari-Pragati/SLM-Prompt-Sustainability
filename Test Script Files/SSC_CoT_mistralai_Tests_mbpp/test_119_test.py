import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), 15)
        self.assertEqual(search([10, 20, 30, 40, 50]), 145)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(search([0]), 0)
        self.assertEqual(search([1]), 1)
        self.assertEqual(search([1, 0]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6]), 127)
        self.assertEqual(search([10, 20, 30, 40, 50, 60]), 3127)
        self.assertEqual(search([-1, 0, 1]), -1)
        self.assertEqual(search([1000000000, 2000000000, 3000000000, 4000000000, 5000000000]), 1073741823)

    def test_special_and_corner_cases(self):
        self.assertEqual(search([1, 2, 3, 2, 1]), 0)
        self.assertEqual(search([1, 2, 3, 2, 1, 2]), 1)
        self.assertEqual(search([1, 1, 1, 1, 1]), 0)
        self.assertEqual(search([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(search([0, 0, 0, 0, 0]), 0)

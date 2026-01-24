import unittest
from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):

    def test_add_K_element(self):
        self.assertEqual(add_K_element([(1, 2), (3, 4)], 5), [(6, 7), (8, 9)])
        self.assertEqual(add_K_element([(10, 20), (30, 40)], 0), [(10, 20), (30, 40)])
        self.assertEqual(add_K_element([(-1, -2), (-3, -4)], 5), [ (4, 3), (2, 1)])
        self.assertEqual(add_K_element([], 5), [])

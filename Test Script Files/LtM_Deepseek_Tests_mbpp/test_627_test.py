import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 5, 6, 7, 8, 9], 0, 8), 4)

    def test_edge_conditions(self):
        self.assertEqual(find_First_Missing([1], 0, 0), 1)
        self.assertEqual(find_First_Missing([0], 0, 0), 1)
        self.assertEqual(find_First_Missing([], 0, -1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10), 11)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 0, 10), 10)

    def test_complex_cases(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 6, 7, 8, 9], 0, 8), 5)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 7, 8, 9], 0, 8), 6)

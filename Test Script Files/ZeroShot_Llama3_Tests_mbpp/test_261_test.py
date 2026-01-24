import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_division_elements(self):
        self.assertEqual(division_elements((10, 2, 3), (2, 3, 4)), (5, 1, 0))
        self.assertEqual(division_elements((10, 2, 3), (3, 2, 4)), (3, 1, 0))
        self.assertEqual(division_elements((10, 2, 3), (4, 2, 3)), (2, 1, 1))
        self.assertEqual(division_elements((10, 2, 3), (2, 3, 4)), (5, 1, 0))
        self.assertEqual(division_elements((10, 2, 3), (3, 4, 2)), (3, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (4, 3, 2)), (2, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (2, 4, 3)), (5, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (3, 4, 3)), (3, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (4, 4, 2)), (2, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (2, 4, 3)), (5, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (3, 4, 3)), (3, 0, 1))
        self.assertEqual(division_elements((10, 2, 3), (4, 4, 3)), (2, 0, 1))

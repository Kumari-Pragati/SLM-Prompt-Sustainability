import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_division_elements(self):
        self.assertEqual(division_elements((7, 3, 4), (3, 2, 1)), (2, 3, 4))
        self.assertEqual(division_elements((1, 2, 3), (1, 2, 4)), (1, 1, 0))
        self.assertEqual(division_elements((5, 10, 15), (5, 2, 3)), (1, 5, 5))

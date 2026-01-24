import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), ((-2, 0, 2),))
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3)), ((0, 0, 0),))
        self.assertEqual(substract_elements((1, 2, 3), ()), ())
        self.assertEqual(substract_elements((), (1, 2, 3)), ())
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6, 7)), ((-3, -3, -3),))
        self.assertEqual(substract_elements((1, 2, 3, 4), (1, 2, 3)), ((0, 0, 1),))
        self.assertEqual(substract_elements((1, 2, 3, 4, 5), (1, 2, 3, 4),), ((0, 0, 1, 1),))

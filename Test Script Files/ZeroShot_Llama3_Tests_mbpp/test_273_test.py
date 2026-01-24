import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), (2, 4, 2))
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3)), (0, 0, 0))
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), (-5, -7, -9))
        self.assertEqual(substract_elements((1, 2, 3), ()), ())
        self.assertEqual(substract_elements((), (1, 2, 3)), ())
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3, 4)), (-3, -2, -3))

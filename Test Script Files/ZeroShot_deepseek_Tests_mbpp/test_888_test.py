import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))
        self.assertEqual(substract_elements((10, 20, 30), (5, 15, 25)), ((5, 5, 5),))
        self.assertEqual(substract_elements((100, 200, 300), (10, 20, 30)), ((90, 180, 270),))

    def test_substract_elements_with_different_lengths(self):
        self.assertEqual(substract_elements((1, 2, 3, 4), (4, 5, 6)), ((-3, -3, -3), (4,)))
        self.assertEqual(substract_elements((10, 20, 30), (5, 15, 25, 30)), ((5, 5, 5), (30,)))

    def test_substract_elements_with_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())
        self.assertEqual(substract_elements((1, 2, 3), ()), ((1, 2, 3),))
        self.assertEqual(substract_elements((), (1, 2, 3)), ((-1, -2, -3),))

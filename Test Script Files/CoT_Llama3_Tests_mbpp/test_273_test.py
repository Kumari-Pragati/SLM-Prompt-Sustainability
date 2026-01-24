import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), (2, 4, 2))
        self.assertEqual(substract_elements((1, 2, 3), (1, 2, 3)), (0, 0, 0))

    def test_substract_elements_empty(self):
        self.assertRaises(IndexError, substract_elements, (), (1, 2, 3))

    def test_substract_elements_diff_length(self):
        self.assertRaises(IndexError, substract_elements, (1, 2), (1, 2, 3))

    def test_substract_elements_negative(self):
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), (-5, -7, -9))

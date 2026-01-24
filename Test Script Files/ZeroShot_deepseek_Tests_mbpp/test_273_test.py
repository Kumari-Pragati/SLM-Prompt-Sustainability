import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 20, 30), (5, 10, 15)), (5, 10, 15))
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), (-3, -3, -3))
        self.assertEqual(substract_elements((100, 200, 300), (100, 200, 300)), (0, 0, 0))
        self.assertEqual(substract_elements((-1, -2, -3), (-4, -5, -6)), (3, 3, 3))
        self.assertEqual(substract_elements((10, 20, 30), (10, 20, 30)), (0, 0, 0))

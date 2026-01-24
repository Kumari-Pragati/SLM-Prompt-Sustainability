import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(substract_elements((1, 2, 3), (1, 0, 1)), (0, 2, 2))
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), (-1, -2, -3))
        self.assertEqual(substract_elements((4, 4, 4), (1, 1, 1)), (3, 3, 3))

    def test_edge_cases(self):
        self.assertEqual(substract_elements((0,), (1,)), (-1,))
        self.assertEqual(substract_elements((1,), (0,)), (1,))
        self.assertEqual(substract_elements((0, 0), (0, 0)), (0, 0))
        self.assertEqual(substract_elements((1, 2, 3), (0, 0, 0)), (1, 2, 3))
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), (-1, -2, -3))

    def test_complex(self):
        self.assertEqual(substract_elements((100, -200, 300), (-100, 200, -300)), (200, -400, 600))
        self.assertEqual(substract_elements((sys.maxsize,), (sys.maxsize - 1,)), (-1,))
        self.assertEqual(substract_elements((sys.maxsize - 1,), (sys.maxsize,)), (sys.maxsize - 1,))

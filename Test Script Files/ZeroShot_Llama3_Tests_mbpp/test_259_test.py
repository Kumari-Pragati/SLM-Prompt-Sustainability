import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_maximize_elements(self):
        self.assertEqual(maximize_elements((1, 2), (3, 4)), ((3, 2),))
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5, 6)), ((6, 5, 3),))
        self.assertEqual(maximize_elements((1, 2, 3, 4), (5, 6, 7, 8)), ((8, 7, 7, 4),))
        self.assertEqual(maximize_elements((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)), ((10, 8, 8, 5, 4),))
        self.assertEqual(maximize_elements((1, 2, 3, 4, 5, 6), (7, 8, 9, 10, 11, 12)), ((12, 11, 9, 8, 6, 5),))

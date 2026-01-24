import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_find_exponentio(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (8, 25))
        self.assertEqual(find_exponentio((5, 2), (3, 7)), (125, 343))
        self.assertEqual(find_exponentio((10, 1), (2, 3)), (10, 2))
        self.assertEqual(find_exponentio((0, 0), (2, 3)), (0, 0))

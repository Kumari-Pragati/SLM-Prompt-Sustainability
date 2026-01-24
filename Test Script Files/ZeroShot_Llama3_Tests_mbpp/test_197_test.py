import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_find_exponentio(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (16, 25))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), (1, 16))
        self.assertEqual(find_exponentio((5, 6), (7, 8)), (15625, 65536))
        self.assertEqual(find_exponentio((0, 0), (1, 2)), (0, 1))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), (1, 16))
        self.assertEqual(find_exponentio((5, 6), (7, 8)), (15625, 65536))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), (1, 16))
        self.assertEqual(find_exponentio((5, 6), (7, 8)), (15625, 65536))
        self.assertEqual(find_exponentio((0, 0), (1, 2)), (0, 1))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), (1, 16))
        self.assertEqual(find_exponentio((5, 6), (7, 8)), (15625, 65536))

import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_count_X(self):
        self.assertEqual(count_X((1, 2, 3), 1), 1)
        self.assertEqual(count_X((1, 2, 3), 2), 1)
        self.assertEqual(count_X((1, 2, 3), 3), 1)
        self.assertEqual(count_X((1, 2, 3), 4), 0)
        self.assertEqual(count_X((1, 2, 2, 3, 3), 2), 2)
        self.assertEqual(count_X((1, 2, 2, 3, 3), 1), 1)
        self.assertEqual(count_X((1, 2, 2, 3, 3), 3), 2)
        self.assertEqual(count_X((1, 2, 2, 3, 3), 4), 0)

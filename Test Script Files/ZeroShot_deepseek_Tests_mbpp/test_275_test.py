import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_get_Position(self):
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 2), 2)
        self.assertEqual(get_Position([15, 25, 35, 45], 4, 5), 1)
        self.assertEqual(get_Position([100, 200, 300, 400], 4, 10), 4)
        self.assertEqual(get_Position([1, 2, 3, 4], 4, 1), 1)
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 10), 1)
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 20), 1)

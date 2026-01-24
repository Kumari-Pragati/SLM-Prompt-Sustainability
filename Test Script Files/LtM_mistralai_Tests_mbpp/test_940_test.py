import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(shift_down([1, 3, 2]), [1, 2, 3])
        self.assertEqual(shift_down([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shift_down([2, 3, 1]), [1, 2, 3])

    def test_edge_cases(self):
        self.assertEqual(shift_down([1]), [1])
        self.assertEqual(shift_down([1, 2]), [2, 1])
        self.assertEqual(shift_down([1, 2, 3]), [1, 2, 3])
        self.assertEqual(shift_down([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shift_down([3, 2, 1, 4]), [1, 2, 3, 4])

    def test_complex(self):
        self.assertEqual(shift_down([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(shift_down([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shift_down([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shift_down([5, 1, 3, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shift_down([3, 5, 1, 2, 4]), [1, 2, 3, 4, 5])

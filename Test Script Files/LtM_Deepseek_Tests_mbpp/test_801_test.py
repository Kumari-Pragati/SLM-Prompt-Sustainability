import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    # Test for simple / typical inputs
    def test_three_equal_typical(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    # Test for edge and boundary conditions
    def test_three_equal_edge(self):
        self.assertEqual(test_three_equal(0, 0, 0), 0)
        self.assertEqual(test_three_equal(-1, -1, -1), 0)
        self.assertEqual(test_three_equal(1000, 1000, 1000), 0)

    # Test for more complex or corner cases
    def test_three_equal_complex(self):
        self.assertEqual(test_three_equal(1, 2, 2), 1)
        self.assertEqual(test_three_equal(1, 1, 2), 1)
        self.assertEqual(test_three_equal(1, 2, 3), 1)
        self.assertEqual(test_three_equal(0, 0, 1), 2)

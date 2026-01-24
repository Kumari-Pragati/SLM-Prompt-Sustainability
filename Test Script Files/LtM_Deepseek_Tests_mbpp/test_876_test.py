import unittest
from mbpp_876_code import lcm

class TestLCM(unittest.TestCase):

    # Test for simple / typical inputs
    def test_lcm_typical(self):
        self.assertEqual(lcm(10, 15), 30)
        self.assertEqual(lcm(2, 7), 14)

    # Test for edge and boundary conditions
    def test_lcm_edge(self):
        self.assertEqual(lcm(0, 15), 0)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(2, 2), 2)

    # Test for more complex or corner cases
    def test_lcm_complex(self):
        self.assertEqual(lcm(100, 200), 200)
        self.assertEqual(lcm(3, 6), 6)
        self.assertEqual(lcm(15, 21), 105)

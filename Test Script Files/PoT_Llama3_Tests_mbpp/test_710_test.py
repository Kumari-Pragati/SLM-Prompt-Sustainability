import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(front_and_rear((1, 2, 3)), (1, 3))

    def test_edge(self):
        self.assertEqual(front_and_rear(()), ())
        self.assertEqual(front_and_rear((1,)), (1,))

    def test_edge2(self):
        self.assertEqual(front_and_rear((1, 2)), (1, 2))

    def test_edge3(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4)), (1, 4))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            front_and_rear("test")

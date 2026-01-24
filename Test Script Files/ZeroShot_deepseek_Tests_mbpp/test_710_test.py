import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_front_and_rear(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), ((1, 5)))
        self.assertEqual(front_and_rear(('a', 'b', 'c', 'd', 'e')), (('a', 'e')))
        self.assertEqual(front_and_rear((10, 20, 30, 40, 50)), ((10, 50)))
        self.assertEqual(front_and_rear(('apple', 'banana', 'cherry', 'date', 'elderberry')), (('apple', 'elderberry')))

import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(2.5), 23.25)

    def test_edge_input(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(-1), None)
        self.assertEqual(dog_age(21), 21)
        self.assertEqual(dog_age(22), 64.5)

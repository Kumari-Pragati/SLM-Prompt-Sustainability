import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25)
        self.assertEqual(dog_age(4), 29)

    def test_edge(self):
        self.assertEqual(dog_age(-1), None)
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(100), 114)

    def test_complex(self):
        self.assertEqual(dog_age(5), 29)
        self.assertEqual(dog_age(10), 54)
        self.assertEqual(dog_age(20), 99)

import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25.5)

    def test_edge_cases(self):
        self.assertEqual(dog_age(-1), None)
        self.assertEqual(dog_age(200), 221)
        self.assertEqual(dog_age(float('inf')), 221)

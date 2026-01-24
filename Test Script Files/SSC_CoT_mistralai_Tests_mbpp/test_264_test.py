import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25.5)

    def test_edge_cases(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(2.000001), 21.00004)
        self.assertEqual(dog_age(21), 63)
        self.assertEqual(dog_age(21.00001), 63.00004)

    def test_negative_input(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_multiple_tuple(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)
        self.assertEqual(mutiple_tuple((4, 5, 6)), 120)
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)
        self.assertEqual(mutiple_tuple((0, 0, 0)), 0)
        self.assertEqual(mutiple_tuple((-1, 0, 0)), 0)
        self.assertEqual(mutiple_tuple((1, 2, 3, 4)), 24)
        self.assertEqual(mutiple_tuple((-1, 2, 3, 4)), -24)
        self.assertEqual(mutiple_tuple((1, 2, 3, 4, 5)), 120)
        self.assertEqual(mutiple_tuple((-1, 2, 3, 4, 5)), -120)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            mutiple_tuple((1, 2, 'a', 4))

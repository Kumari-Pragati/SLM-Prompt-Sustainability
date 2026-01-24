import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_multiple_to_single(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)
        self.assertEqual(multiple_to_single([4, 5, 6]), 456)
        self.assertEqual(multiple_to_single([7, 8, 9]), 789)
        self.assertEqual(multiple_to_single([10, 20, 30]), 1030)
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(multiple_to_single([10, 20, 30, 40, 50]), 103045)
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5, 6]), 123456)
        self.assertEqual(multiple_to_single([10, 20, 30, 40, 50, 60]), 10304560)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiple_to_single("hello")
        with self.assertRaises(TypeError):
            multiple_to_single([1, 2, "3"])
        with self.assertRaises(TypeError):
            multiple_to_single([1, 2, 3, "4", 5])

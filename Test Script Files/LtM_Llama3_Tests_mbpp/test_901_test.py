import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 24)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 60)

        self.assertEqual(smallest_multiple(11), 1326)
        self.assertEqual(smallest_multiple(12), 132)
        self.assertEqual(smallest_multiple(13), 2602)
        self.assertEqual(smallest_multiple(14), 348)
        self.assertEqual(smallest_multiple(15), 360)

        self.assertEqual(smallest_multiple(16), 48)
        self.assertEqual(smallest_multiple(17), 28928)
        self.assertEqual(smallest_multiple(18), 216)
        self.assertEqual(smallest_multiple(19), 4374)
        self.assertEqual(smallest_multiple(20), 120)

        self.assertEqual(smallest_multiple(21), 2520)
        self.assertEqual(smallest_multiple(22), 462)
        self.assertEqual(smallest_multiple(23), 29908)
        self.assertEqual(smallest_multiple(24), 144)
        self.assertEqual(smallest_multiple(25), 300)

        self.assertEqual(smallest_multiple(26), 312)
        self.assertEqual(smallest_multiple(27), 378)
        self.assertEqual(smallest_multiple(28), 784)
        self.assertEqual(smallest_multiple(29), 8704)
        self.assertEqual(smallest_multiple(30), 30)

    def test_edge_cases(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 24)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 60)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_multiple("a")
        with self.assertRaises(TypeError):
            smallest_multiple(None)

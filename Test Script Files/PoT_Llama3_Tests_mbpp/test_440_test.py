import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly"), ((14, 24, "slowly")))

    def test_edge_case(self):
        self.assertEqual(find_adverb_position("I am going to the store"), None)

    def test_edge_case2(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly quickly"), ((14, 24, "slowly"), (25, 35, "quickly")))

    def test_edge_case3(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly slowly"), ((14, 24, "slowly"), (25, 35, "slowly")))

    def test_edge_case4(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly slowly slowly"), ((14, 24, "slowly"), (25, 35, "slowly"), (36, 46, "slowly")))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)

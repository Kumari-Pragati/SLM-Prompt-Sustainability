import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_adverbs("She quietly sings the song loudly."), "18-24: loudly")
        self.assertEqual(find_adverbs("He runs quickly."), "18-24: quickly")
        self.assertEqual(find_adverbs("The cat jumps high."), "21-26: high")

    def test_edge_cases(self):
        self.assertEqual(find_adverbs("She sings the song."), "")
        self.assertEqual(find_adverbs("She sings the song loudly, loudly."), "33-38: loudly, loudly")
        self.assertEqual(find_adverbs("She sings the song loudly, very loudly."), "33-38: loudly")
        self.assertEqual(find_adverbs("She sings the song loudly, not loudly."), "33-38: loudly")

    def test_boundary_conditions(self):
        self.assertEqual(find_adverbs("She sings the song ly."), "4-9: ly")
        self.assertEqual(find_adverbs("She sings the song lylylyly."), "10-15: lylylyly")
        self.assertEqual(find_adverbs("She sings the song lylylylylyly."), "10-15: lylylyly")

    def test_invalid_input(self):
        self.assertEqual(find_adverbs(123), "")
        self.assertEqual(find_adverbs(None), "")
        self.assertEqual(find_adverbs(""), "")
        self.assertEqual(find_adverbs("She sings the lylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylylyly
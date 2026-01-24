import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):
    def test_typical_use_case(self):
        text = "aeroplane aerobic aeronaut aeronautical"
        self.assertEqual(words_ae(text), ['aeroplane', 'aerobic', 'aeronaut', 'aeronautical'])

    def test_edge_case(self):
        text = "ae"
        self.assertEqual(words_ae(text), ['ae'])

    def test_boundary_case(self):
        text = "a"
        self.assertEqual(words_ae(text), ['a'])
        text = "e"
        self.assertEqual(words_ae(text), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            words_ae(123)
        with self.assertRaises(TypeError):
            words_ae(None)

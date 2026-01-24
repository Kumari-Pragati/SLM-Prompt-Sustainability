import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(access_key({"key1": "value1", "key2": "value2"}, "key1"), "value1")

    def test_edge_input(self):
        self.assertEqual(access_key({"key1": "value1", "key2": "value2"}, 0), "key1")
        self.assertEqual(access_key({"key1": "value1", "key2": "value2"}, len({"key1": "value1", "key2": "value2"})), "key2")

    def test_boundary_input(self):
        self.assertEqual(access_key({"key1": "value1", "key2": "value2"}, -1), "key1")
        self.assertEqual(access_key({"key1": "value1", "key2": "value2"}, len({"key1": "value1", "key2": "value2"}) + 1), "key2")

    def test_invalid_input(self):
        self.assertRaises(KeyError, access_key, {"key1": "value1", "key2": "value2"}, "invalid_key")

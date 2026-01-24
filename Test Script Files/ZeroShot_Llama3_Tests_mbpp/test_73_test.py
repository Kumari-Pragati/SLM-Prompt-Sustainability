import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_multiple_split(self):
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n"), ["Hello", "World", " Foo", "Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), ["Hello", "World, Foo*Bar"])
        self.assertEqual(multiple_split("Hello;World, Foo*Bar\n\n\n\n\n\n
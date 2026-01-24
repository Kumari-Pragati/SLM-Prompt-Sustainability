import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):

    def test_replace_max_specialchar(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello: World!")
        self.assertEqual(replace_max_specialchar("Hello, World! How are you?", 2), "Hello: World! How: are : you?")
        self.assertEqual(replace_max_specialchar("Hello, World! How are you? I am fine.", 3), "Hello: World! How: are : you? I : am : fine.")
        self.assertEqual(replace_max_specialchar("Hello, World! How are you? I am fine. I am good.", 4), "Hello: World! How: are : you? I : am : fine. I : am : good.")
        self.assertEqual(replace_max_specialchar("Hello, World! How are you? I am fine. I am good. I am great.", 5), "Hello: World! How: are : you? I : am : fine. I : am : good. I : am : great.")
        self.assertEqual(replace_max_specialchar("Hello, World! How are you? I am fine. I am good. I am great. I am awesome.", 6), "Hello: World! How: are : you? I : am : fine. I : am : good. I : am : great. I : am : awesome.")

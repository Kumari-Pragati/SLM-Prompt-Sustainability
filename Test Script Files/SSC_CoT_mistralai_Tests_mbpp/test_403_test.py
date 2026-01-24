import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.org"))
        self.assertTrue(is_valid_URL("http://www.example.net"))

    def test_edge_cases(self):
        self.assertTrue(is_valid_URL("http://example.co.uk"))
        self.assertTrue(is_valid_URL("https://www.example.com.au"))
        self.assertTrue(is_valid_URL("http://example.com.br"))

    def test_short_url(self):
        self.assertTrue(is_valid_URL("http://a"))
        self.assertTrue(is_valid_URL("https://www.b"))
        self.assertTrue(is_valid_URL("http://c.d"))

    def test_long_url(self):
        long_url = "http://a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z"
        self.assertTrue(is_valid_URL(long_url))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL(""))
        self.assertFalse(is_valid_URL("http://example"))
        self.assertFalse(is_valid_URL("http://example.com."))
        self.assertFalse(is_valid_URL("http://example.com@"))
        self.assertFalse(is_valid_URL("http://example.com/"))
        self.assertFalse(is_valid_URL("http://example.com//"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/spaces"))
        self.assertFalse(is_valid_URL("http://example.com/path/with%20spaces"))
        self.assertFalse(is_valid_URL("http://example.com/path/with_underscores"))
        self.assertFalse(is_valid_URL("http://example.com/path/with-hyphens"))
        self.assertFalse(is_valid_URL("http://example.com/path/with+pluses"))
        self.assertFalse(is_valid_URL("http://example.com/path/with=equals"))
        self.assertFalse(is_valid_URL("http://example.com/path/with?query"))
        self.assertFalse(is_valid_URL("http://example.com/path/with#hash"))
        self.assertFalse(is_valid_URL("http://example.com/path/with%61non-alphabetical-characters"))

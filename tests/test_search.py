import unittest

from wuodan.wuodan import search_lines


class TestSearchLines(unittest.TestCase):
    def test_multiple_matches(self):
        lines = ["foo", "bar foo", "baz foo"]
        matches = search_lines(lines, "dummy.txt", "foo")
        self.assertEqual(len(matches), 3)
        self.assertIn("line 1", matches[0])
        self.assertIn("line 2", matches[1])
        self.assertIn("line 3", matches[2])


if __name__ == "__main__":
    unittest.main()

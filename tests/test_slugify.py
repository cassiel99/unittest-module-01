import unittest

from qautils.slugify import slugify


class TestSlugify(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(slugify("Hello"), "hello")

    def test_spaces_replaced_with_dash(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_special_chars_removed(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_multiple_spaces_collapsed(self):
        self.assertEqual(slugify("  multiple   spaces  "), "multiple-spaces")

    def test_underscore_replaced(self):
        self.assertEqual(slugify("Already_Slug"), "already-slug")

    def test_dashes_at_borders(self):
        self.assertEqual(slugify("---A---B---"), "a-b")

    def test_only_special_chars(self):
        self.assertEqual(slugify("!!!"), "")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_numbers_kept(self):
        self.assertEqual(slugify("test 42"), "test-42")

    def test_mixed_underscores_and_spaces(self):
        self.assertEqual(slugify("foo _ bar"), "foo-bar")

    def test_tabs_removed(self):
        self.assertEqual(slugify("foo\tbar"), "foobar")


if __name__ == "__main__":
    unittest.main()

import unittest

from text_analyzer import analyze_text,count_words


class TestTextAnalyzer(unittest.TestCase):

    def test_analyze_text(self):
        result = analyze_text("Hello Python\nHello Git")

        self.assertEqual(result["characters"], 22)
        self.assertEqual(result["words"], 4)
        self.assertEqual(result["lines"], 2)

    def test_empty_text(self):
        result = analyze_text("")

        self.assertEqual(result["characters"], 0)
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["lines"], 0)

    def test_count_words(self):
        result = count_words("hello python hello")

        self.assertEqual(result, {"hello": 2, "python": 1})


    def test_count_words_case_sensitive(self):
        result = count_words("Python python")

        self.assertEqual(result, {"Python": 1, "python": 1})


    def test_count_words_empty_text(self):
        result = count_words("")

        self.assertEqual(result, {})
if __name__ == "__main__":
    unittest.main()

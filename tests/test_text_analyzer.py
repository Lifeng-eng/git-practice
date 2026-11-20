import unittest

from text_analyzer import analyze_text


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


if __name__ == "__main__":
    unittest.main()

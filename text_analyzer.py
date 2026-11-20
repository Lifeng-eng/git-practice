def analyze_text(text: str) -> dict:
    """Analyze basic statistics of a text."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
    }


def count_characters(text: str) -> dict:
    """Count the frequency of each character."""
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def count_words(text: str) -> dict:
    """Count the frequency of each word."""
    frequency = {}

    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

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

def analyze_text(text: str) -> dict:
    """Analyze basic statistics of a text."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
    }

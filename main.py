from text_analyzer import analyze_text


def main():
    text = input("Enter some text: ")

    result = analyze_text(text)

    print("\nText Analysis")
    print("-------------")
    print(f"Characters: {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Lines: {result['lines']}")


if __name__ == "__main__":
    main()
# A small Python text analyzer

import sys

def text_analyzer(text = ""):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if text == "":
        text = input("What is the text to analyse?")
    print("The text contains", len(text), "characters:")
    print("-", sum(1 for c in text if c.isupper()), "upper letter(s)")
    print("-", sum(1 for c in text if c.islower()), "lower letter(s)")
    print("-", sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"), "punctuation mark(s)")
    print("-", sum(1 for c in text if c.isspace()), "space(s)")

def main():
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv) == 1:
        text_analyzer()
    else:
        print("ERROR")

if __name__ == "__main__":
    main()
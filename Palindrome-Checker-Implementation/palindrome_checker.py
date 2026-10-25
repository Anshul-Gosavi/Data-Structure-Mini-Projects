"""Check text for palindromes by comparing a stack and a queue."""


def clean_text(text):
    letters_and_numbers = []

    for character in text:
        if character.isalnum():
            letters_and_numbers.append(character.lower())

    return "".join(letters_and_numbers)


def check_text(text):
    cleaned = clean_text(text)

    if cleaned == "":
        return cleaned, None

    stack = []
    queue = []

    for character in cleaned:
        stack.append(character)
        queue.append(character)

    queue_front = 0
    matches = True

    while len(stack) > 0:
        last_character = stack.pop()
        first_character = queue[queue_front]
        queue_front += 1

        if last_character != first_character:
            matches = False
            break

    return cleaned, matches


def main():
    print("PALINDROME TESTER")
    print("Checking text with a stack and a queue")

    while True:
        entered_text = input("\nType a word or sentence: ")
        cleaned, result = check_text(entered_text)

        if result is None:
            print("There were no letters or numbers to check.")
        else:
            print("Text being checked:", cleaned)
            if result:
                print("This text is a palindrome.")
            else:
                print("This text is not a palindrome.")

        answer = input("Try another one? (y/n): ").strip().lower()
        if answer != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
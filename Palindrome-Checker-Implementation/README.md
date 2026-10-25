# Palindrome Tester: Stack and Queue

## Aim
Check whether a word or sentence reads the same forward and backward by using a stack and a queue.

## Data Structures
A stack follows LIFO (Last In, First Out). The program adds characters with `append()` and takes the most recently added character with `pop()`.

A queue follows FIFO (First In, First Out). Characters are added in order. A front position moves through the list from the first character to the last.

## How the Check Works
The program changes letters to lowercase and ignores spaces, punctuation, and other characters that are not letters or numbers. It places each remaining character in both lists. It then compares characters taken from the top of the stack with characters read from the front of the queue. Matching pairs mean the text is a palindrome.

## Algorithm
1. Read text from the user.
2. Keep only letters and numbers, and make them lowercase.
3. If no characters remain, show a message.
4. Add every character to the stack list and queue list.
5. Remove a character from the end of the stack and read one from the queue's front.
6. If a pair differs, the text is not a palindrome.
7. Display the result and ask whether to check another text.

## Pseudocode
```text
READ text
clean text by keeping lowercase letters and numbers
IF cleaned text is empty:
    DISPLAY message
ELSE:
    CREATE empty stack and queue
    FOR each character:
        ADD character to stack
        ADD character to queue
    SET queue front to first position
    WHILE stack is not empty:
        TAKE last character from stack
        READ character at queue front
        MOVE queue front forward
        IF characters differ:
            mark text as not a palindrome
    DISPLAY result
```

## Example
`Was it a rat I saw?` becomes `wasitaratisaw`, which is a palindrome. `coding` is not a palindrome.

## Complexity
For `n` letters and numbers, the checking loop takes `O(n)` time. The stack and queue each store the characters, so the space use is `O(n)`.

## Run
Use Python 3 to run:

```text
python palindrome_test.py
```

No external packages are required.
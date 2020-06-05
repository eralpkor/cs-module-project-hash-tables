import re

    # remove ignored chars

unwanted_chars =  '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

def word_count(s):
    words = s.lower()

    # whitespace chars to space
    white_space = '\n \t \r'.split(' ')

    for target_list in white_space:
        words = words.replace(target_list, ' ')

    for char in unwanted_chars:
        words = words.replace(char, '')

    # turn string into an array of words
    words = words.split(' ')

    seen_words = {}

    for w in words:
        # skip empty
        if w == '':
            continue

        if w in seen_words:
            seen_words[w] += 1
        else:
            seen_words[w] = 1

    return seen_words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

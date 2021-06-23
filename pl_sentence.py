def pl_sentence():
    """
    A pig latin translator 2.0. Takes a simple sentence and then outputs the pig latin translator of it.
    """
    raw_input = input("Enter the text to be translated: ").lower().strip()
    split_word = raw_input.split()
    for word in split_word:
        if word[0] in 'aeiou':
            print(f'{word}way'.title(), end=' ')
            # return f'{word}way'.title()
        else:
            print(f'{word[1:]}{word[0]}ay'.title(), end=" ")
            # return f'{word[1:]}{character}ay'.title()


pl_sentence()
def ubbi_dubbi(word):
    """
    Function takes a word as an argument and output the "ubbi dubbi" translation.
    The idea is to add 'ub' before every vowel sound in the word.
    """
    output = []
    for letter in word.lower():
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    dubbed_word = ''.join(output)
    return dubbed_word.title()


print(ubbi_dubbi('Python'))

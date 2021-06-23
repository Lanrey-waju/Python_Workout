def pig_latin():
    """
    This program takes a word as an input and then outputs the pig latin interpretation
    """
    raw_word = input("Enter word: ").lower().strip()
    # above code strips the input of any whitespace and also renders the string in lowercase
    if raw_word[0] in 'aeiou':
        return f'{raw_word.title()}way'

    else:
        return f"{raw_word[1:].title()}{raw_word[0]}ay"


pig_latin()

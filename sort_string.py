def strsort(seq):
    """Takes a string (sequence) and returns a string"""
    return "".join(sorted(seq))


# print(strsort("wyfgilkdpsjw"))


def sort_and_comma(seq):
    """
    Break a given sentence into individual words, and then sort
    those words alphabetically before printing the words separated by comma
    seq: str
    Returns: str
    """
    sorted_words = sorted(seq.split())
    return ", ".join(sorted_words)


# print(sort_and_comma("World Hello Dick Harry"))


def find_last_word():
    with open("dev.txt", "r") as f:
        data = sorted(f.read().split())
        print(data[-1])


# find_last_word()


def get_max_length(word):
    return len(word)


def find_longest_word():
    with open("dev.txt", "r") as f:
        data = f.read().split()
    print(sorted(data, key=get_max_length)[-1])


find_longest_word()

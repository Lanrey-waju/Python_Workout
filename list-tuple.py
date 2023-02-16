def firstlast(seq):
    """
    Takes an iterable and returns the first and last element in a
    two-element sequence of the same type
    """
    return seq[:1] + seq[-1:]


print(firstlast([1, 2, 3, 4]))

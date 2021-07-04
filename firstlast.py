import operator


def firstLast(iterable):
    """
    A program to return the first and the last items in an iterable
    :param iterable: string, list, tuple
    :return: first and last occurrence in the iterable
    """
    outcome = operator.itemgetter(0, -1)
    return outcome(iterable)


print(firstLast([0, 2, 3, 5]))

#another way to implement the idea is by using slices
def firstLast2(sequence):
    return sequence[:1] + sequence[-1:]

print(firstLast2([1, 2, 3, 4, 6]))
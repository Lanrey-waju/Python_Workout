def even_odd_sums(sequence):
    """
    function takes a list or tipple and returns a two_element list
    :return: [sum of odd-indexed numbers, sum of even-indexed numbers]
    """
    even_sum = sum(sequence[0::2])
    odd_sum = sum(sequence[1::2])
    return odd_sum, even_sum


print(even_odd_sums([0, 1, 2, 3, 4, 5, 6, 7]))
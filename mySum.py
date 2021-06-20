# A function to simulate the in_built sum function

def my_sum(numbers, begin=0):
    """returns the sum of the positional arguments given"""
    result = begin
    for number in numbers:
        result += number
    print(result)
    return result


my_sum([100, 200, 300, 600])

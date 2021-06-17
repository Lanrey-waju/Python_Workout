# A function to simulate the in_built sum function

def my_sum(*numbers):
    """returns the sum of the positional arguments given"""
    result = 0
    for number in numbers:
        result += number
    print(result)
    return result


my_sum(100, 200, 300, 400)

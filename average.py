# A program that takes a list of numbers and output their average

def average(numbers):
    base_number = 0
    for number in numbers:
        base_number += number
    mean_of_numbers = base_number/len(numbers)
    print(mean_of_numbers)
    return mean_of_numbers


average([1,2,3,4])
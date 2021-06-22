def name_triangle():
    """
    function collects a user's name as input and outputs parts of the name un successive lines until name is completed
    """
    index = 0
    triangle = ''
    name = input("Enter your first name: ").strip()
    for character in name:
        triangle += name[index]
        print(triangle)
        # print(name[index])
        index += 1
        if index == len(name):
            break


name_triangle()

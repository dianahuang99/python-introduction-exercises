def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    endNum = stop + 1

    for num in range(start, endNum):
        print(num)

    # YOUR CODE HERE


count_up(5, 7)


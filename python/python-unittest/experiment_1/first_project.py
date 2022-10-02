# calculate the average of a list of numbers
def avg(*list_numbers: float):
    total = 0
    for num in list_numbers:

        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("Wrong input data")

    return total / len(list_numbers)

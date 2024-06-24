def mean(numbers):
    """Compute the average of a set of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a set of numbers."""
    if len(numbers) == 0:
        return 0

    sortednumbers = sorted(numbers)
    n = len(sortednumbers)

    if n % 2 == 0:
        # Even number of elements, average the two middle ones
        return (sortednumbers[n//2 - 1] + sortednumbers[n//2]) / 2
    else:
        # Odd number of elements, return the middle one
        return sorted_numbers[n//2]

def mode(numbers):
    """Compute the mode of a set of numbers."""
    if len(numbers) == 0:
        return 0

    count_dict = {}
    max_count = 0
    modes = []

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

        if count_dict[num] > max_count:
            max_count = count_dict[num]
            modes = [num]
        elif count_dict[num] == max_count:
            modes.append(num)

    return modes

def main():
    numbers = [4, 9, 3, 7, 5, 8, 6, 2, 1]
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode(s):", mode(numbers))

if __name == "__main":
    main()